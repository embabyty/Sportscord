#!/usr/bin/env python3
"""Generate the 30 NBA Vencord themes from official team colors and logos."""
import json
from pathlib import Path

import build as shared

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'themes' / 'nba'
ROSTER = ROOT / 'tools' / 'nba_teams.json'
LOGO_BASE = (
    f'https://raw.githubusercontent.com/embabyty/NFLcord/{shared.LOGO_BRANCH}/assets/logos/nba'
)


def main():
    teams = json.loads(ROSTER.read_text(encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    for t in teams:
        accent = t['accent'].upper()
        primary = t['primary'].upper()
        secondary = t['secondary'].upper()
        link = t['link'].upper()
        hover = (
            shared.mix_hex(accent, '#000000', .10)
            if shared.luminance(accent) >= .35
            else shared.mix_hex(accent, '#FFFFFF', .14)
        )
        active = (
            shared.mix_hex(accent, '#000000', .20)
            if shared.luminance(accent) >= .35
            else shared.mix_hex(accent, '#FFFFFF', .26)
        )
        text = (
            '#FFFFFF'
            if shared.contrast(accent, '#FFFFFF') >= shared.contrast(accent, '#000000')
            else '#000000'
        )
        tint = primary if primary not in ('#000000', '#FFFFFF') else accent
        link_name = t.get('linkName', t['secondaryName'])
        accent_name = t.get(
            'accentName',
            t['primaryName'] if accent == primary else t['secondaryName'],
        )
        colorway = (
            f'{accent_name} {accent} throughout'
            if link == accent
            else f'{accent_name} {accent} with {link_name} {link}'
        )
        css = shared.TEMPLATE.substitute(
            name=t['name'], abbr=t['abbr'], division=f"{t['division']} Division",
            primary=primary, secondary=secondary, accent=accent, hover=hover,
            active=active, accentText=text, tint=tint, link=link,
            linkName=link_name, accentName=accent_name, colorway=colorway,
            logoUrl=f"{LOGO_BASE}/{t['slug']}.png",
            sidebarDark=shared.mix_hex(tint, shared.SIDEBAR_DARK_BASE, 1 - shared.SIDEBAR_DARK_RATIO),
            sidebarLight=shared.mix_hex(tint, shared.SIDEBAR_LIGHT_BASE, 1 - shared.SIDEBAR_LIGHT_RATIO),
            accentHsl=shared.hex_to_hsl_triplet(accent),
            hoverHsl=shared.hex_to_hsl_triplet(hover),
            activeHsl=shared.hex_to_hsl_triplet(active),
        )
        css = (
            css.replace('NFLcord', 'NBAcord')
            .replace('https://github.com/embabyty/NBAcord', 'https://github.com/embabyty/NFLcord')
            .replace('https://raw.githubusercontent.com/embabyty/NBAcord/', 'https://raw.githubusercontent.com/embabyty/NFLcord/')
            .replace('all 32 NFL teams', 'all 30 NBA teams')
            .replace('NFL collection', 'NBA collection')
            .replace('--nfl-', '--nba-')
        )
        (OUT / f"{t['slug']}.theme.css").write_text(css, encoding='utf-8')
    print(f'Generated {len(teams)} NBA themes in {OUT}')


if __name__ == '__main__':
    main()
