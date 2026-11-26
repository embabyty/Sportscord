#!/usr/bin/env python3
"""Generate Unbound iOS/Android themes for every Sportscord team.

Unbound themes are not CSS: each addon is a folder with a manifest.json and a
bundle.json holding a palette of Discord semantic/raw color overrides. See
https://unbound.rip/docs/developer/themes/introduction for the format.

Run:  python tools/build_unbound.py
Output:
  themes/unbound/nfl/<slug>/{manifest.json,bundle.json}
  themes/unbound/nba/<slug>/{manifest.json,bundle.json}
  themes/unbound/ncaaf/<slug>/{manifest.json,bundle.json}
  themes/unbound/README.md  (install links for every theme)
"""
import json
from pathlib import Path

import build as shared

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "themes" / "unbound"
NBA_ROSTER = ROOT / "tools" / "nba_teams.json"
NCAAF_ROSTER = ROOT / "tools" / "ncaaf_teams.json"

# raw.githubusercontent.com links install straight into Unbound: the iOS
# "Install from URL" action reads manifest.json and its sibling bundle.json.
# Keep the branch in sync with build.py's logo host.
RAW_BASE = (
    f"https://raw.githubusercontent.com/embabyty/NFLcord/{shared.LOGO_BRANCH}/themes/unbound"
)

# Dark, team-tinted surfaces. Small tint ratios keep text readable while the
# team color still comes through on every panel.
SURFACES = {
    "lowest": ("#000000", 0.06),
    "lower": ("#0A0A0F", 0.09),
    "low": ("#121218", 0.11),
    "base": ("#181820", 0.12),
    "high": ("#22222C", 0.13),
    "highest": ("#2B2B36", 0.14),
}


def alpha(color: str, fraction: float) -> str:
    """Append an alpha byte to a #RRGGBB color (Unbound accepts #RRGGBBAA)."""
    return color + f"{round(max(0, min(1, fraction)) * 255):02X}"


def readable(color: str, against: str = "#0B0B10", target: float = 4.5) -> str:
    """Lift a dark team color toward white until it is legible on dark surfaces."""
    if shared.contrast(color, against) >= target:
        return color
    for amount in (0.15, 0.30, 0.45, 0.60, 0.75, 0.90):
        lifted = shared.mix_hex(color, "#FFFFFF", amount)
        if shared.contrast(lifted, against) >= target:
            return lifted
    return "#FFFFFF"


def text_on(color: str) -> str:
    """Pick black or white for text sitting on a team-colored fill."""
    return (
        "#FFFFFF"
        if shared.contrast(color, "#FFFFFF") >= shared.contrast(color, "#000000")
        else "#000000"
    )


def palette(accent: str, tint: str, link: str) -> dict:
    """Build the semantic/raw palette for one team (dark base)."""
    accent = accent.upper()
    tint = tint.upper() if tint.upper() not in ("#000000", "#FFFFFF") else accent
    link = link.upper()

    surface = {name: shared.mix_hex(base, tint, ratio) for name, (base, ratio) in SURFACES.items()}
    brand = readable(accent, target=3.0)  # actionable brand color on a dark UI
    brand_text = text_on(brand)

    a = lambda fraction: alpha(accent, fraction)  # noqa: E731 - local shorthand
    w = lambda fraction: alpha("#FFFFFF", fraction)  # noqa: E731 - local shorthand

    semantic = {
        # App background tiers
        "BACKGROUND_BASE_LOWEST": surface["lowest"],
        "BACKGROUND_BASE_LOWER": surface["lower"],
        "BACKGROUND_BASE_LOW": surface["low"],
        "BACKGROUND_PRIMARY": surface["lower"],
        "BACKGROUND_SECONDARY": surface["base"],
        "BACKGROUND_SECONDARY_ALT": surface["low"],
        "BACKGROUND_TERTIARY": surface["low"],
        "BACKGROUND_FLOATING": surface["high"],
        "BACKGROUND_NESTED_FLOATING": surface["highest"],
        "BACKGROUND_SURFACE_HIGH": surface["high"],
        "BACKGROUND_SURFACE_HIGHEST": surface["highest"],
        "BACKGROUND_MOBILE_PRIMARY": surface["lower"],
        "BACKGROUND_MOBILE_SECONDARY": surface["base"],
        "BACKGROUND_ACCENT": shared.mix_hex(surface["high"], accent, 0.22),
        "BACKGROUND_BRAND": brand,
        "BACKGROUND_SCRIM": alpha(shared.mix_hex("#000000", tint, 0.20), 0.80),
        "BLUR_FALLBACK": alpha(surface["lower"], 0.96),
        "BLUR_FALLBACK_PRESSED": alpha(surface["high"], 0.96),
        "PANEL_BG": surface["base"],
        "CARD_BACKGROUND_DEFAULT": surface["high"],
        "MODAL_BACKGROUND": surface["high"],
        "CARD_BORDER_DEFAULT": w(0.12),
        "BORDER_SUBTLE": w(0.08),
        "BORDER_NORMAL": w(0.12),
        "BORDER_MUTED": w(0.18),
        "BORDER_STRONG": w(0.30),
        "BORDER_FOCUS": brand,
        "APP_FRAME_BORDER": w(0.12),
        # Channel list, chat and composer
        "CHANNEL_BACKGROUND_DEFAULT": surface["lower"],
        "CHANNELS_DEFAULT": "#A8ABB5",
        "CHANNEL_ICON": "#82858F",
        "CHAT_BACKGROUND": surface["low"],
        "CHAT_BANNER_BG": surface["low"],
        "CHAT_BORDER": w(0.08),
        "CHANNELTEXTAREA_BACKGROUND": surface["base"],
        "CHAT_INPUT_BACKGROUND": surface["base"],
        "CHAT_INPUT_ICON_DEFAULT_TINT": "#A8ABB5",
        "CHAT_INPUT_SEND_BUTTON_ACTIVE_BACKGROUND": brand,
        "CHAT_INPUT_SEND_BUTTON_ICON_ACTIVE_TINT": brand_text,
        "MOBILE_CHATINPUT_BACKGROUND_DEFAULT": surface["base"],
        "MOBILE_CHATINPUT_BACKGROUND_ACTIVE": shared.mix_hex(surface["base"], accent, 0.12),
        "MOBILE_CHANNEL_ITEM_BACKGROUND_SELECTED": a(0.45),
        "MOBILE_HEADER_BORDER": w(0.08),
        "MOBILE_EMBED_BACKGROUND_DEFAULT": surface["high"],
        "MOBILE_TYPING_INDICATOR_BACKGROUND_DEFAULT": surface["base"],
        "MOBILE_VOICE_PANEL_BACKGROUND": surface["base"],
        "KEYBOARD": surface["lower"],
        "ANDROID_NAVIGATION_BAR_BACKGROUND": surface["low"],
        # Selected rows, hovers, mentions and highlights in team color
        "BACKGROUND_MOD_MUTED": a(0.14),
        "BACKGROUND_MOD_SUBTLE": a(0.10),
        "BACKGROUND_MOD_NORMAL": a(0.20),
        "BACKGROUND_MOD_STRONG": a(0.33),
        "BACKGROUND_MODIFIER_HOVER": a(0.20),
        "BACKGROUND_MODIFIER_ACTIVE": a(0.33),
        "BACKGROUND_MODIFIER_SELECTED": a(0.60),
        "BACKGROUND_MENTIONED": a(0x1F / 255),
        "MESSAGE_BACKGROUND_HOVER": a(0.08),
        "MESSAGE_MENTIONED_BACKGROUND_DEFAULT": a(0x1F / 255),
        "MENTION_BACKGROUND": a(0.33),
        "MENTION_FOREGROUND": readable(accent, target=4.5),
        # Text
        "TEXT_DEFAULT": "#F2F3F5",
        "TEXT_NORMAL": "#F2F3F5",
        "TEXT_STRONG": "#FFFFFF",
        "TEXT_MUTED": "#A8ABB5",
        "TEXT_SUBTLE": "#82858F",
        "TEXT_LINK": readable(link),
        "TEXT_BRAND": readable(accent),
        "HEADER_PRIMARY": "#F2F3F5",
        "HEADER_SECONDARY": "#A8ABB5",
        "INPUT_TEXT_DEFAULT": "#F2F3F5",
        "MOBILE_TEXT_HEADING_PRIMARY": "#F2F3F5",
        # Icons and interactive states
        "ICON_DEFAULT": "#A8ABB5",
        "ICON_MUTED": "#82858F",
        "ICON_SUBTLE": "#6D7079",
        "ICON_BRAND": readable(accent),
        "INTERACTIVE_NORMAL": "#A8ABB5",
        "INTERACTIVE_HOVER": "#F2F3F5",
        "INTERACTIVE_ACTIVE": "#FFFFFF",
        "INTERACTIVE_MUTED": "#6D7079",
        "INTERACTIVE_ICON_DEFAULT": "#A8ABB5",
        "INTERACTIVE_ICON_HOVER": "#F2F3F5",
        "INTERACTIVE_ICON_ACTIVE": "#FFFFFF",
        "INTERACTIVE_TEXT_DEFAULT": "#A8ABB5",
        "INTERACTIVE_TEXT_HOVER": "#F2F3F5",
        "INTERACTIVE_TEXT_ACTIVE": "#FFFFFF",
        "INTERACTIVE_BACKGROUND_HOVER": w(0.08),
        "INTERACTIVE_BACKGROUND_ACTIVE": w(0.13),
        "INTERACTIVE_BACKGROUND_SELECTED": a(0.33),
        # Controls, buttons and badges
        "CONTROL_BRAND_FOREGROUND": brand,
        "CONTROL_BRAND_FOREGROUND_NEW": brand,
        "SWITCH_BACKGROUND_SELECTED_DEFAULT": brand,
        "CHECKBOX_BACKGROUND_SELECTED_DEFAULT": brand,
        "CHECKBOX_BORDER_SELECTED_DEFAULT": brand,
        "CHECKBOX_ICON_ACTIVE": brand_text,
        "BUTTON_OUTLINE_BRAND_BACKGROUND_HOVER": a(0.20),
        "BUTTON_OUTLINE_BRAND_BORDER_ACTIVE": brand,
        "BUTTON_OUTLINE_PRIMARY_TEXT": readable(accent),
        "BADGE_PRIMARY_BACKGROUND": brand,
        "BADGE_PRIMARY_BORDER": brand,
        "BADGE_PRIMARY_TEXT": brand_text,
        "MOBILE_SEGMENTED_CONTROL_INDICATOR_BACKGROUND": brand,
        # Mobile panels
        "MOBILE_ACTIONSHEET_BACKGROUND": surface["high"],
        "MOBILE_ALERT_BACKGROUND_DEFAULT": surface["high"],
        "MOBILE_TOAST_BACKGROUND_DEFAULT": surface["high"],
        "MOBILE_FLOATINGBAR_BACKGROUND": surface["base"],
        "MOBILE_COMMAND_BAR_BACKGROUND": surface["base"],
    }

    # Raw colors sit below semantic roles: brand keys take the team color,
    # primary keys the neutral surfaces (matching Discord's own palette use).
    raw = {
        "BLURPLE_50": readable(accent),
        "BLURPLE_65": brand,
        "BRAND_260": readable(accent),
        "BRAND_500": brand,
        "BRAND_900": shared.mix_hex(surface["lowest"], accent, 0.30),
        "BRAND_NEW_500_ALPHA_20": a(0.20),
        "PRIMARY_100": "#F2F3F5",
        "PRIMARY_200": "#C9CBD2",
        "PRIMARY_300": "#A8ABB5",
        "PRIMARY_360": "#82858F",
        "PRIMARY_400": surface["high"],
        "PRIMARY_500": surface["base"],
        "PRIMARY_600": surface["low"],
        "PRIMARY_630": surface["low"],
        "PRIMARY_700": surface["lower"],
        "PRIMARY_800": surface["lowest"],
        "PRIMARY_DARK_500_ALPHA_20": alpha(surface["lowest"], 0.20),
        "PRIMARY_DARK_700_ALPHA_60": alpha(surface["lower"], 0.60),
        "DANGER": "#F23F43",
        "GREEN_600": "#23A55A",
        "RED_400": "#F23F43",
        "YELLOW_300": "#F0B232",
    }

    return {
        "type": "midnight",
        "semantic": {name: {"type": "color", "value": value} for name, value in semantic.items()},
        "raw": raw,
    }


def colorway(team: dict) -> str:
    accent = team["accent"].upper()
    link = team["link"].upper()
    if accent == link:
        return f"{accent} throughout"
    return f"{accent} accents with {link} links"


def addon(team: dict, league: str) -> dict:
    slug = team["slug"]
    return {
        "id": f"sportscord.{league}.{slug}".replace("_", "-"),
        "name": f"Sportscord • {team['name']}",
        "description": (
            f"{team['name']} ({team['abbr']}) — {colorway(team)}. "
            f"Unofficial fan theme for Unbound."
        ),
        "authors": [{"name": "Sportscord", "id": "0"}],
        "version": "1.0.0",
        "main": "bundle.json",
    }


def write_team(team: dict, league: str) -> str:
    folder = OUT / league / team["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    accent = team["accent"].upper()
    tint = team.get("tint", team["primary"]).upper()
    (folder / "manifest.json").write_text(
        json.dumps(addon(team, league), indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (folder / "bundle.json").write_text(
        json.dumps(palette(accent, tint, team["link"]), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return f"{RAW_BASE}/{league}/{team['slug']}/manifest.json"


def index_table(rows: list) -> str:
    lines = ["| Team | Abbr | Install (manifest URL) |", "| ---- | ---- | ---------------------- |"]
    lines += [f"| {name} | {abbr} | [`Install from URL`]({url}) |" for name, abbr, url in rows]
    return "\n".join(lines)


def main() -> None:
    import build

    nfl = []
    for team in build.TEAMS:
        url = write_team(team, "nfl")
        nfl.append((team["name"], team["abbr"], url))

    nba = []
    for team in json.loads(NBA_ROSTER.read_text(encoding="utf-8")):
        url = write_team(team, "nba")
        nba.append((team["name"], team["abbr"], url))

    ncaaf = []
    for team in json.loads(NCAAF_ROSTER.read_text(encoding="utf-8")):
        url = write_team(team, "ncaaf")
        ncaaf.append((team["name"], team["abbr"], url))

    readme = f"""# Sportscord for Unbound (iOS / Android)

[Unbound](https://unbound.rip/) runs inside the official Discord app on iOS
(with or without a jailbreak) and on Android. These are Unbound themes built
from the same team colors as the Vencord collection.

## Install

1. Install Unbound into Discord using the [iOS](https://unbound.rip/docs/user/installing)
   or Android instructions. Open Discord's settings and confirm the **Unbound**
   section appears.
2. In Discord: **Settings → Unbound → Design → Themes → + → Install from URL**.
3. Paste a manifest URL from the tables below and tap Install.
4. Tap the new card to apply it, then **restart Discord**. Only one theme is
   applied at a time; tap it again to return to Discord's own colors.

Themes are dark (Onyx/\"midnight\" base) and use the team accent for brand
buttons, selected channel rows, mentions, badges, focus rings and controls,
with each theme's link color (usually the secondary team color) for links.
Edit any `bundle.json` and reinstall to tweak the palette; colors you leave
out keep Discord's defaults.

If the default branch is renamed, update `RAW_BASE` in `tools/build_unbound.py`
and rebuild — the URLs below are generated from it.

## NFL ({len(nfl)})

{index_table(nfl)}

## NBA ({len(nba)})

{index_table(nba)}

## NCAAF ({len(ncaaf)})

{index_table(ncaaf)}

Regenerate everything with:

```sh
python3 tools/build_unbound.py
```
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")
    print(
        f"Generated {len(nfl)} NFL + {len(nba)} NBA + {len(ncaaf)} NCAAF "
        f"Unbound themes in {OUT}"
    )


if __name__ == "__main__":
    main()
