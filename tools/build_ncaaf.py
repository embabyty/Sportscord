#!/usr/bin/env python3
"""Generate 2026 NCAAF FBS Vencord themes from the shared NFLcord design."""
import json
from pathlib import Path
import build as shared

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'themes' / 'ncaaf'
ROSTER = ROOT / 'tools' / 'ncaaf_teams.json'
LOGO_BASE = 'https://raw.githubusercontent.com/embabyty/NFLcord/vencord/assets/logos/ncaaf'


def main():
    teams = json.loads(ROSTER.read_text(encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    for t in teams:
        accent = t['primary'].upper()
        hover = shared.mix_hex(accent, '#000000', .10) if shared.luminance(accent) >= .35 else shared.mix_hex(accent, '#FFFFFF', .14)
        active = shared.mix_hex(accent, '#000000', .20) if shared.luminance(accent) >= .35 else shared.mix_hex(accent, '#FFFFFF', .26)
        text = '#FFFFFF' if shared.contrast(accent, '#FFFFFF') >= shared.contrast(accent, '#000000') else '#000000'
        secondary = t['secondary'].upper()
        tint = accent if accent not in ('#000000', '#FFFFFF') else secondary
        css = shared.TEMPLATE.substitute(
            name=t['name'], abbr=t['abbr'], division='2026 FBS',
            primary=accent, secondary=secondary, accent=accent, hover=hover,
            active=active, accentText=text, tint=tint, link=secondary,
            linkName='Secondary', colorway=f'{accent} with {secondary}',
            accentName='Primary', logoUrl=f"{LOGO_BASE}/{t['slug']}.png",
            sidebarDark=shared.mix_hex(tint, shared.SIDEBAR_DARK_BASE, 1-shared.SIDEBAR_DARK_RATIO),
            sidebarLight=shared.mix_hex(tint, shared.SIDEBAR_LIGHT_BASE, 1-shared.SIDEBAR_LIGHT_RATIO),
            accentHsl=shared.hex_to_hsl_triplet(accent),
            hoverHsl=shared.hex_to_hsl_triplet(hover),
            activeHsl=shared.hex_to_hsl_triplet(active),
        )
        css = css.replace('NFLcord', 'NCAAFcord').replace('https://github.com/embabyty/NCAAFcord', 'https://github.com/embabyty/NFLcord').replace('https://raw.githubusercontent.com/embabyty/NCAAFcord/', 'https://raw.githubusercontent.com/embabyty/NFLcord/').replace('all 32 NFL teams', '2026 FBS teams').replace('NFL collection', 'NCAAF collection').replace('--nfl-', '--cfb-')
        (OUT / f"{t['slug']}.theme.css").write_text(css, encoding='utf-8')
    print(f'Generated {len(teams)} themes in {OUT}')

if __name__ == '__main__':
    main()
