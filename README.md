# NFLcord Themes

Vencord themes for all **32 NFL teams**, each dressed in its official team colors.
Pick your team, drop the file into Vencord, and Discord buttons, mentions,
links, badges, and highlights take on your team's identity. Works in both
dark and light mode.

## Install

**Vencord (desktop):**

1. Download or clone this repo.
2. In Discord, go to `Settings → Themes → Open Themes Folder`.
3. Copy `themes/<your-team>.theme.css` into that folder.
4. Back in `Settings → Themes`, enable it. Use only one NFLcord theme at a time.

**Vencord (web):**

1. Go to `Settings → Themes → Upload Theme` and select your team's file.

**BetterDiscord:** the files use the standard `.theme.css` header format, so they
can also be dropped into BetterDiscord's `themes` folder.

## Vesktop background material (Acrylic)

These themes support transparency, so Vesktop's
`Settings → Window → Background Material` setting works with them —
your blurred desktop wallpaper shows through the backdrop and glass panels:

1. Set Background Material to `Acrylic` (or another transparent effect).
2. Fully restart Discord from the tray — required after changing the setting.
3. In Vencord QuickCSS (`Settings → Themes → QuickCSS`), lower the backdrop
   opacity so the wallpaper comes through:

```css
:root {
  --glass-opacity: 0.55;
}
```

Values around `0.45–0.65` look best; `1` (default) is fully opaque.
On clients without a transparency setting, lowering it just deepens
the backdrop, so it is safe to experiment.

### Full-transparency preset (dark acrylic)

For the full see-through look with text kept readable, use
[`presets/full-transparent-dark-acrylic.css`](presets/full-transparent-dark-acrylic.css).
Easiest option — paste this as the **very first line** of your QuickCSS:

```css
@import url("https://raw.githubusercontent.com/embabyty/NFLcord/vencord/presets/full-transparent-dark-acrylic.css");
```

Or paste the preset's contents at the **end** of your QuickCSS.
It drops the backdrop to ~35% and thins the panels/chat/popouts/inputs
while keeping them solid enough to read over a dark wallpaper
(use a dark wallpaper — bright ones will wash text out).
Tune the percentages in the file to taste: higher = more solid.

## macOS support

The themes work on macOS with no extra setup. macOS intentionally uses
the opaque team-tinted surfaces — no Mica, vibrancy, or extra blur is
added. On `platform-osx` the themes pin `--glass-opacity` to `1` (so any
Windows acrylic tuning is ignored), switch the frosted panels off
`backdrop-filter`, and keep the native traffic lights clickable with a
draggable title bar plus macOS font smoothing. Team colors, the home-button
logo, and layout are unchanged.

On macOS the UI font switches to
[Google Sans](https://fonts.google.com/specimen/Google+Sans) (weights
400/500/700, loaded from Google Fonts at the top of each theme file);
other platforms keep Discord's default font.

## Customize

Every theme exposes its palette as CSS variables, so you can tweak it in
Vencord QuickCSS (`Settings → Themes → QuickCSS`) without editing the file:

```css
:root {
  --nfl-accent: #ff0000;      /* buttons, badges, brand */
  --nfl-accent-text: #ffffff; /* text on the accent */
  --nfl-link: #ff0000;        /* links */
  --nfl-logo: url("https://i.imgur.com/your-image.png"); /* home button */
  --nfl-sidebar: #1a2b3c !important; /* channel list background */
  --glass-blur: 28px; /* frosted-glass strength */
  --glass-radius: 18px; /* glass panel corner roundness */
}
```

> Note: custom `--nfl-logo` URLs must be hosted on Vencord's allowlist
> (GitHub, Imgur, etc.), otherwise Discord blocks them from loading.

## Themes

| Team | Abbr | Division | Accent | Secondary |
| ---- | ---- | -------- | ------ | --------- |
| [Arizona Cardinals](themes/arizona-cardinals.theme.css) | ARI | NFC West | Cardinal Red `#97233F` | Desert Gold `#FFB612` |
| [Atlanta Falcons](themes/atlanta-falcons.theme.css) | ATL | NFC South | Red `#A71930` | Silver `#A5ACAF` |
| [Baltimore Ravens](themes/baltimore-ravens.theme.css) | BAL | AFC North | Purple `#241773` | Metallic Gold `#9E7C0C` |
| [Buffalo Bills](themes/buffalo-bills.theme.css) | BUF | AFC East | Royal Blue `#00338D` | Red `#C60C30` |
| [Carolina Panthers](themes/carolina-panthers.theme.css) | CAR | NFC South | Panther Blue `#0085CA` | Silver `#BFC0BF` |
| [Chicago Bears](themes/chicago-bears.theme.css) | CHI | NFC North | Burnt Orange `#C83803` | Midnight Navy `#0B162A` |
| [Cincinnati Bengals](themes/cincinnati-bengals.theme.css) | CIN | AFC North | Orange `#FB4F14` | Black `#000000` |
| [Cleveland Browns](themes/cleveland-browns.theme.css) | CLE | AFC North | Orange `#FF3C00` | Brown `#311D00` |
| [Dallas Cowboys](themes/dallas-cowboys.theme.css) | DAL | NFC East | Royal Blue `#003594` | Silver `#869397` |
| [Denver Broncos](themes/denver-broncos.theme.css) | DEN | AFC West | Orange `#FB4F14` | Navy `#002244` |
| [Detroit Lions](themes/detroit-lions.theme.css) | DET | NFC North | Honolulu Blue `#0076B6` | Silver `#B0B7BC` |
| [Green Bay Packers](themes/green-bay-packers.theme.css) | GB | NFC North | Dark Green `#203731` | Gold `#FFB612` |
| [Houston Texans](themes/houston-texans.theme.css) | HOU | AFC South | Battle Red `#A71930` | Deep Steel Blue `#03202F` |
| [Indianapolis Colts](themes/indianapolis-colts.theme.css) | IND | AFC South | Speed Blue `#002C5F` | Gray `#A2AAAD` |
| [Jacksonville Jaguars](themes/jacksonville-jaguars.theme.css) | JAX | AFC South | Teal `#006778` | Gold `#D7A22A` |
| [Kansas City Chiefs](themes/kansas-city-chiefs.theme.css) | KC | AFC West | Red `#E31837` | Gold `#FFB81C` |
| [Las Vegas Raiders](themes/las-vegas-raiders.theme.css) | LV | AFC West | Silver `#A5ACAF` | Black `#000000` |
| [Los Angeles Chargers](themes/los-angeles-chargers.theme.css) | LAC | AFC West | Powder Blue `#0080C6` | Sunshine Gold `#FFC20E` |
| [Los Angeles Rams](themes/los-angeles-rams.theme.css) | LAR | NFC West | Royal Blue `#003594` | Sol Yellow `#FFA300` |
| [Miami Dolphins](themes/miami-dolphins.theme.css) | MIA | AFC East | Aqua `#008E97` | Orange `#FC4C02` |
| [Minnesota Vikings](themes/minnesota-vikings.theme.css) | MIN | NFC North | Purple `#4F2683` | Gold `#FFC62F` |
| [New England Patriots](themes/new-england-patriots.theme.css) | NE | AFC East | Red `#C60C30` | Nautical Blue `#002244` |
| [New Orleans Saints](themes/new-orleans-saints.theme.css) | NO | NFC South | Old Gold `#D3BC8D` | Black `#101820` |
| [New York Giants](themes/new-york-giants.theme.css) | NYG | NFC East | Blue `#0B2265` | Red `#A71930` |
| [New York Jets](themes/new-york-jets.theme.css) | NYJ | AFC East | Gotham Green `#125740` | White `#FFFFFF` |
| [Philadelphia Eagles](themes/philadelphia-eagles.theme.css) | PHI | NFC East | Midnight Green `#004C54` | Silver `#A5ACAF` |
| [Pittsburgh Steelers](themes/pittsburgh-steelers.theme.css) | PIT | AFC North | Gold `#FFB612` | Black `#101820` |
| [San Francisco 49ers](themes/san-francisco-49ers.theme.css) | SF | NFC West | 49ers Red `#AA0000` | Gold `#B3995D` |
| [Seattle Seahawks](themes/seattle-seahawks.theme.css) | SEA | NFC West | Action Green `#69BE28` | College Navy `#002244` |
| [Tampa Bay Buccaneers](themes/tampa-bay-buccaneers.theme.css) | TB | NFC South | Red `#D50A0A` | Bucco Orange `#FF7900` |
| [Tennessee Titans](themes/tennessee-titans.theme.css) | TEN | AFC South | Titans Blue `#4B92DB` | Titans Red `#C8102E` |
| [Washington Commanders](themes/washington-commanders.theme.css) | WSH | NFC East | Burgundy `#5A1414` | Gold `#FFB612` |

## NCAAF Themes (2026 FBS)

The NCAAF collection brings the same glass styling, accent controls, links,
channel highlights, and team logo home button to all 138 programs competing in
FBS during the 2026 season. Enable one NCAAF theme at a time. Install a file
from `themes/ncaaf/` with the same Vencord/BetterDiscord steps above.

Regenerate the collection with:

```sh
python3 tools/build_ncaaf.py
```

Team colors and logo paths are recorded in `tools/ncaaf_teams.json`; the
logo images are in `assets/logos/ncaaf/`, so builds do not need network access. The logos are
third-party team marks; this remains an unofficial fan project.

| Team | Abbr | Accent | Secondary |
| ---- | ---- | ------ | --------- |
| [Air Force Falcons](themes/ncaaf/air-force-falcons.theme.css) | AF | `#003594` | `#FFFFFF` |
| [Akron Zips](themes/ncaaf/akron-zips.theme.css) | AKR | `#041E42` | `#C5B783` |
| [Alabama Crimson Tide](themes/ncaaf/alabama-crimson-tide.theme.css) | ALA | `#9E1B32` | `#FFFFFF` |
| [Appalachian State Mountaineers](themes/ncaaf/appalachian-state-mountaineers.theme.css) | APP | `#FFC520` | `#FFCD00` |
| [Arizona Wildcats](themes/ncaaf/arizona-wildcats.theme.css) | ARIZ | `#CC0033` | `#003366` |
| [Arizona State Sun Devils](themes/ncaaf/arizona-state-sun-devils.theme.css) | ASU | `#FFC627` | `#8C1D40` |
| [Arkansas Razorbacks](themes/ncaaf/arkansas-razorbacks.theme.css) | ARK | `#A32136` | `#FFFFFF` |
| [Arkansas State Red Wolves](themes/ncaaf/arkansas-state-red-wolves.theme.css) | ARST | `#CC092F` | `#000000` |
| [Army Black Knights](themes/ncaaf/army-black-knights.theme.css) | ARMY | `#D19D00` | `#D3BC8D` |
| [Auburn Tigers](themes/ncaaf/auburn-tigers.theme.css) | AUB | `#002B5C` | `#F26522` |
| [Ball State Cardinals](themes/ncaaf/ball-state-cardinals.theme.css) | BALL | `#BA0C2F` | `#FFFFFF` |
| [Baylor Bears](themes/ncaaf/baylor-bears.theme.css) | BAY | `#154734` | `#FFB81C` |
| [Boise State Broncos](themes/ncaaf/boise-state-broncos.theme.css) | BOIS | `#0033A0` | `#D64309` |
| [Boston College Eagles](themes/ncaaf/boston-college-eagles.theme.css) | BC | `#8C2232` | `#DBCCA6` |
| [Bowling Green Falcons](themes/ncaaf/bowling-green-falcons.theme.css) | BGSU | `#FD5000` | `#4F2C1D` |
| [Buffalo Bulls](themes/ncaaf/buffalo-bulls.theme.css) | BUF | `#005BBB` | `#FFFFFF` |
| [BYU Cougars](themes/ncaaf/byu-cougars.theme.css) | BYU | `#0047BA` | `#002E5D` |
| [California Golden Bears](themes/ncaaf/california-golden-bears.theme.css) | CAL | `#041E42` | `#FFC72C` |
| [Central Michigan Chippewas](themes/ncaaf/central-michigan-chippewas.theme.css) | CMU | `#4C0027` | `#FBAB18` |
| [Charlotte 49ers](themes/ncaaf/charlotte-49ers.theme.css) | CLT | `#005035` | `#A49665` |
| [Cincinnati Bearcats](themes/ncaaf/cincinnati-bearcats.theme.css) | CIN | `#FD0026` | `#E00122` |
| [Clemson Tigers](themes/ncaaf/clemson-tigers.theme.css) | CLEM | `#F56600` | `#FFFFFF` |
| [Coastal Carolina Chanticleers](themes/ncaaf/coastal-carolina-chanticleers.theme.css) | CCU | `#006F71` | `#A27752` |
| [Colorado Buffaloes](themes/ncaaf/colorado-buffaloes.theme.css) | COLO | `#CFB87C` | `#000000` |
| [Colorado State Rams](themes/ncaaf/colorado-state-rams.theme.css) | CSU | `#004C23` | `#C8C372` |
| [Delaware Fightin’ Blue Hens](themes/ncaaf/delaware-fightin-blue-hens.theme.css) | DEL | `#00539F` | `#FFD200` |
| [Duke Blue Devils](themes/ncaaf/duke-blue-devils.theme.css) | DUKE | `#00539B` | `#FFFFFF` |
| [East Carolina Pirates](themes/ncaaf/east-carolina-pirates.theme.css) | ECU | `#582C83` | `#FFC72C` |
| [Eastern Michigan Eagles](themes/ncaaf/eastern-michigan-eagles.theme.css) | EMU | `#006938` | `#FFFFFF` |
| [FIU Panthers](themes/ncaaf/fiu-panthers.theme.css) | FIU | `#091F3F` | `#C3993F` |
| [Florida Gators](themes/ncaaf/florida-gators.theme.css) | FLA | `#0021A5` | `#FA4616` |
| [Florida Atlantic Owls](themes/ncaaf/florida-atlantic-owls.theme.css) | FAU | `#003366` | `#CC0000` |
| [Florida State Seminoles](themes/ncaaf/florida-state-seminoles.theme.css) | FSU | `#782F40` | `#CEB888` |
| [Fresno State Bulldogs](themes/ncaaf/fresno-state-bulldogs.theme.css) | FRES | `#B1102B` | `#13284C` |
| [Georgia Bulldogs](themes/ncaaf/georgia-bulldogs.theme.css) | UGA | `#BA0C2F` | `#2C2A29` |
| [Georgia Southern Eagles](themes/ncaaf/georgia-southern-eagles.theme.css) | GASO | `#041E42` | `#A3AAAE` |
| [Georgia State Panthers](themes/ncaaf/georgia-state-panthers.theme.css) | GAST | `#0039A6` | `#FFFFFF` |
| [Georgia Tech Yellow Jackets](themes/ncaaf/georgia-tech-yellow-jackets.theme.css) | GT | `#B3A369` | `#FFFFFF` |
| [Hawaii Rainbow Warriors](themes/ncaaf/hawaii-rainbow-warriors.theme.css) | HAW | `#005737` | `#000000` |
| [Houston Cougars](themes/ncaaf/houston-cougars.theme.css) | HOU | `#C8102E` | `#FFFFFF` |
| [Illinois Fighting Illini](themes/ncaaf/illinois-fighting-illini.theme.css) | ILL | `#FF5F05` | `#13294B` |
| [Indiana Hoosiers](themes/ncaaf/indiana-hoosiers.theme.css) | IU | `#970310` | `#FFFFFF` |
| [Iowa Hawkeyes](themes/ncaaf/iowa-hawkeyes.theme.css) | IOWA | `#231F20` | `#FCD116` |
| [Iowa State Cyclones](themes/ncaaf/iowa-state-cyclones.theme.css) | ISU | `#AE192D` | `#FFC72A` |
| [Jacksonville State Gamecocks](themes/ncaaf/jacksonville-state-gamecocks.theme.css) | JXST | `#CC0000` | `#000000` |
| [James Madison Dukes](themes/ncaaf/james-madison-dukes.theme.css) | JMU | `#450084` | `#CBB677` |
| [Kansas Jayhawks](themes/ncaaf/kansas-jayhawks.theme.css) | KU | `#0051BA` | `#E8000D` |
| [Kansas State Wildcats](themes/ncaaf/kansas-state-wildcats.theme.css) | KSU | `#330A57` | `#E2E3E4` |
| [Kennesaw State Owls](themes/ncaaf/kennesaw-state-owls.theme.css) | KENN | `#FDBB30` | `#0B1315` |
| [Kent State Golden Flashes](themes/ncaaf/kent-state-golden-flashes.theme.css) | KENT | `#002664` | `#EAAB00` |
| [Kentucky Wildcats](themes/ncaaf/kentucky-wildcats.theme.css) | UK | `#0033A0` | `#FFFFFF` |
| [Liberty Flames](themes/ncaaf/liberty-flames.theme.css) | LIB | `#0A254E` | `#B72025` |
| [Louisiana Ragin’ Cajuns](themes/ncaaf/louisiana-ragin-cajuns.theme.css) | UL | `#CE181E` | `#000000` |
| [Louisiana–Monroe Warhawks](themes/ncaaf/louisiana-monroe-warhawks.theme.css) | ULM | `#840029` | `#FDB913` |
| [Louisiana Tech Bulldogs](themes/ncaaf/louisiana-tech-bulldogs.theme.css) | LT | `#003087` | `#CB333B` |
| [Louisville Cardinals](themes/ncaaf/louisville-cardinals.theme.css) | LOU | `#C9001F` | `#FFFFFF` |
| [LSU Tigers](themes/ncaaf/lsu-tigers.theme.css) | LSU | `#461D76` | `#FDD023` |
| [Marshall Thundering Herd](themes/ncaaf/marshall-thundering-herd.theme.css) | MRSH | `#00B140` | `#000000` |
| [Maryland Terrapins](themes/ncaaf/maryland-terrapins.theme.css) | MD | `#CE1126` | `#FFFFFF` |
| [Memphis Tigers](themes/ncaaf/memphis-tigers.theme.css) | MEM | `#004991` | `#8E908F` |
| [Miami (FL) Hurricanes](themes/ncaaf/miami-fl-hurricanes.theme.css) | MIA | `#F47423` | `#035131` |
| [Miami (OH) RedHawks](themes/ncaaf/miami-oh-redhawks.theme.css) | M-OH | `#C41230` | `#FFFFFF` |
| [Michigan Wolverines](themes/ncaaf/michigan-wolverines.theme.css) | MICH | `#00274C` | `#FFCB05` |
| [Michigan State Spartans](themes/ncaaf/michigan-state-spartans.theme.css) | MSU | `#173F35` | `#FFFFFF` |
| [Middle Tennessee Blue Raiders](themes/ncaaf/middle-tennessee-blue-raiders.theme.css) | MTSU | `#036EB7` | `#FFFFFF` |
| [Minnesota Golden Gophers](themes/ncaaf/minnesota-golden-gophers.theme.css) | MINN | `#5E0A2F` | `#FAB41C` |
| [Mississippi State Bulldogs](themes/ncaaf/mississippi-state-bulldogs.theme.css) | MSST | `#5D1725` | `#C1C6C8` |
| [Missouri Tigers](themes/ncaaf/missouri-tigers.theme.css) | MIZ | `#F1B82D` | `#000000` |
| [Missouri State Bears](themes/ncaaf/missouri-state-bears.theme.css) | MOST | `#5E0009` | `#FFFFFF` |
| [Navy Midshipmen](themes/ncaaf/navy-midshipmen.theme.css) | NAVY | `#00225B` | `#B5A67C` |
| [NC State Wolfpack](themes/ncaaf/nc-state-wolfpack.theme.css) | NCSU | `#CC0000` | `#FFFFFF` |
| [Nebraska Cornhuskers](themes/ncaaf/nebraska-cornhuskers.theme.css) | NEB | `#E31937` | `#FFFFFF` |
| [Nevada Wolf Pack](themes/ncaaf/nevada-wolf-pack.theme.css) | NEV | `#041E42` | `#8A8D8F` |
| [New Mexico Lobos](themes/ncaaf/new-mexico-lobos.theme.css) | UNM | `#BA0C2F` | `#A7A8AA` |
| [New Mexico State Aggies](themes/ncaaf/new-mexico-state-aggies.theme.css) | NMSU | `#7E141B` | `#231F20` |
| [North Carolina Tar Heels](themes/ncaaf/north-carolina-tar-heels.theme.css) | UNC | `#7BAFD4` | `#13294B` |
| [North Dakota State Bison](themes/ncaaf/north-dakota-state-bison.theme.css) | NDSU | `#01402A` | `#FFFFFF` |
| [North Texas Mean Green](themes/ncaaf/north-texas-mean-green.theme.css) | UNT | `#068F33` | `#FFFFFF` |
| [Northern Illinois Huskies](themes/ncaaf/northern-illinois-huskies.theme.css) | NIU | `#C8102E` | `#000000` |
| [Northwestern Wildcats](themes/ncaaf/northwestern-wildcats.theme.css) | NU | `#492F92` | `#FFFFFF` |
| [Notre Dame Fighting Irish](themes/ncaaf/notre-dame-fighting-irish.theme.css) | ND | `#062340` | `#C99700` |
| [Ohio Bobcats](themes/ncaaf/ohio-bobcats.theme.css) | OHIO | `#154734` | `#FFFFFF` |
| [Ohio State Buckeyes](themes/ncaaf/ohio-state-buckeyes.theme.css) | OSU | `#BA0C2F` | `#A8ADB4` |
| [Oklahoma Sooners](themes/ncaaf/oklahoma-sooners.theme.css) | OU | `#990000` | `#FFFFFF` |
| [Oklahoma State Cowboys](themes/ncaaf/oklahoma-state-cowboys.theme.css) | OKST | `#FE5C00` | `#000000` |
| [Old Dominion Monarchs](themes/ncaaf/old-dominion-monarchs.theme.css) | ODU | `#003768` | `#A1D2F1` |
| [Ole Miss Rebels](themes/ncaaf/ole-miss-rebels.theme.css) | MISS | `#13294B` | `#CF142B` |
| [Oregon Ducks](themes/ncaaf/oregon-ducks.theme.css) | ORE | `#00934B` | `#FFF41B` |
| [Oregon State Beavers](themes/ncaaf/oregon-state-beavers.theme.css) | ORST | `#DC4405` | `#000000` |
| [Penn State Nittany Lions](themes/ncaaf/penn-state-nittany-lions.theme.css) | PSU | `#061440` | `#FFFFFF` |
| [Pittsburgh Panthers](themes/ncaaf/pittsburgh-panthers.theme.css) | PITT | `#003594` | `#FFB81C` |
| [Purdue Boilermakers](themes/ncaaf/purdue-boilermakers.theme.css) | PUR | `#CEB888` | `#000000` |
| [Rice Owls](themes/ncaaf/rice-owls.theme.css) | RICE | `#00205B` | `#C1C6C8` |
| [Rutgers Scarlet Knights](themes/ncaaf/rutgers-scarlet-knights.theme.css) | RUTG | `#CE0E2D` | `#FFFFFF` |
| [Sacramento State Hornets](themes/ncaaf/sacramento-state-hornets.theme.css) | SAC | `#00573C` | `#CDB97D` |
| [Sam Houston Bearkats](themes/ncaaf/sam-houston-bearkats.theme.css) | SHSU | `#F56423` | `#FFFFFF` |
| [San Diego State Aztecs](themes/ncaaf/san-diego-state-aztecs.theme.css) | SDSU | `#A6192E` | `#000000` |
| [San Jose State Spartans](themes/ncaaf/san-jose-state-spartans.theme.css) | SJSU | `#0038A8` | `#FFB81A` |
| [SMU Mustangs](themes/ncaaf/smu-mustangs.theme.css) | SMU | `#A80000` | `#0033A1` |
| [South Alabama Jaguars](themes/ncaaf/south-alabama-jaguars.theme.css) | USA | `#00205B` | `#BF0D3E` |
| [South Carolina Gamecocks](themes/ncaaf/south-carolina-gamecocks.theme.css) | SC | `#73000A` | `#000000` |
| [South Florida Bulls](themes/ncaaf/south-florida-bulls.theme.css) | USF | `#006747` | `#CFC493` |
| [Southern Miss Golden Eagles](themes/ncaaf/southern-miss-golden-eagles.theme.css) | USM | `#FFC72C` | `#231F20` |
| [Stanford Cardinal](themes/ncaaf/stanford-cardinal.theme.css) | STAN | `#8C1515` | `#FFFFFF` |
| [Syracuse Orange](themes/ncaaf/syracuse-orange.theme.css) | SYR | `#000E54` | `#FF431B` |
| [TCU Horned Frogs](themes/ncaaf/tcu-horned-frogs.theme.css) | TCU | `#4D1979` | `#FFFFFF` |
| [Temple Owls](themes/ncaaf/temple-owls.theme.css) | TEM | `#A41E35` | `#FFFFFF` |
| [Tennessee Volunteers](themes/ncaaf/tennessee-volunteers.theme.css) | TENN | `#FF8200` | `#FFFFFF` |
| [Texas Longhorns](themes/ncaaf/texas-longhorns.theme.css) | TEX | `#AF5C37` | `#FFFFFF` |
| [Texas A&M Aggies](themes/ncaaf/texas-a-and-m-aggies.theme.css) | TA&M | `#500000` | `#FFFFFF` |
| [Texas State Bobcats](themes/ncaaf/texas-state-bobcats.theme.css) | TXST | `#501214` | `#6A5638` |
| [Texas Tech Red Raiders](themes/ncaaf/texas-tech-red-raiders.theme.css) | TTU | `#DA291C` | `#000000` |
| [Toledo Rockets](themes/ncaaf/toledo-rockets.theme.css) | TOL | `#0B2240` | `#FFCD00` |
| [Troy Trojans](themes/ncaaf/troy-trojans.theme.css) | TROY | `#862633` | `#B1B1B1` |
| [Tulane Green Wave](themes/ncaaf/tulane-green-wave.theme.css) | TULN | `#006747` | `#418FDE` |
| [Tulsa Golden Hurricane](themes/ncaaf/tulsa-golden-hurricane.theme.css) | TLSA | `#003595` | `#D0B787` |
| [UAB Blazers](themes/ncaaf/uab-blazers.theme.css) | UAB | `#1A5632` | `#FDB913` |
| [UCF Knights](themes/ncaaf/ucf-knights.theme.css) | UCF | `#B4985A` | `#B4A169` |
| [UCLA Bruins](themes/ncaaf/ucla-bruins.theme.css) | UCLA | `#2774AE` | `#F2A900` |
| [UConn Huskies](themes/ncaaf/uconn-huskies.theme.css) | CONN | `#0C2340` | `#A2AAAD` |
| [UMass Minutemen](themes/ncaaf/umass-minutemen.theme.css) | MASS | `#881C1C` | `#FFFFFF` |
| [UNLV Rebels](themes/ncaaf/unlv-rebels.theme.css) | UNLV | `#CF0A2C` | `#CAC8C8` |
| [USC Trojans](themes/ncaaf/usc-trojans.theme.css) | USC | `#9D2235` | `#FFC72C` |
| [Utah Utes](themes/ncaaf/utah-utes.theme.css) | UTAH | `#BE0000` | `#FFFFFF` |
| [Utah State Aggies](themes/ncaaf/utah-state-aggies.theme.css) | USU | `#0F2439` | `#FFFFFF` |
| [UTEP Miners](themes/ncaaf/utep-miners.theme.css) | UTEP | `#FF8200` | `#041E42` |
| [UTSA Roadrunners](themes/ncaaf/utsa-roadrunners.theme.css) | UTSA | `#0C2340` | `#F15A22` |
| [Vanderbilt Commodores](themes/ncaaf/vanderbilt-commodores.theme.css) | VAN | `#BB8D09` | `#CFAE70` |
| [Virginia Cavaliers](themes/ncaaf/virginia-cavaliers.theme.css) | UVA | `#232D4B` | `#F84C1E` |
| [Virginia Tech Hokies](themes/ncaaf/virginia-tech-hokies.theme.css) | VT | `#6A2C3E` | `#CF4520` |
| [Wake Forest Demon Deacons](themes/ncaaf/wake-forest-demon-deacons.theme.css) | WAKE | `#CEB888` | `#2C2A29` |
| [Washington Huskies](themes/ncaaf/washington-huskies.theme.css) | WASH | `#33006F` | `#E8D3A2` |
| [Washington State Cougars](themes/ncaaf/washington-state-cougars.theme.css) | WSU | `#A60F2D` | `#4D4D4D` |
| [West Virginia Mountaineers](themes/ncaaf/west-virginia-mountaineers.theme.css) | WVU | `#EAAA00` | `#002855` |
| [Western Kentucky Hilltoppers](themes/ncaaf/western-kentucky-hilltoppers.theme.css) | WKU | `#E13A3E` | `#FFFFFF` |
| [Western Michigan Broncos](themes/ncaaf/western-michigan-broncos.theme.css) | WMU | `#532E1F` | `#F1C500` |
| [Wisconsin Badgers](themes/ncaaf/wisconsin-badgers.theme.css) | WIS | `#A00000` | `#FFFFFF` |
| [Wyoming Cowboys](themes/ncaaf/wyoming-cowboys.theme.css) | WYO | `#492F24` | `#FFC425` |

## What each theme changes

- Team logo as the Discord home button (top of the server list)
- Liquid glass across the whole UI: team-tinted glowing backdrop, frosted
  server rail / channel list / member list (blur, rounded corners, glossy
  highlights), floating translucent chat panel, and translucent headers,
  inputs, popouts, modals, settings, and friends views
- Channel list rows in full team color (solid selected channel, tinted hover/active)
- Hover/active shades derived from the accent for readable feedback
- Links and mentions in the secondary team color
- Soft team-tinted backgrounds for mentions and highlights
- Channel list rows in full team color (solid selected channel, tinted hover/active)
- Text selection in team colors
- On-accent text (black or white) chosen per team for WCAG AA contrast

Surfaces stay translucent rather than fully transparent (roughly 70–85%
opaque), and blur is reserved for the mostly-static outer panels so chat
scrolling stays smooth — the team identity comes through everywhere
without hurting readability.

## Regenerating

All themes are generated from `tools/build.py` (team data + one shared
template), so a fix applies to every team at once:

```sh
python tools/build.py
```

Logos live in `assets/logos/` (one PNG per team) and are loaded from this
repo via `raw.githubusercontent.com`, which is on Vencord's image allowlist —
no extra setup needed once pushed. If the default branch is ever renamed,
update `LOGO_BRANCH` in `tools/build.py` and rebuild.

Team logos are trademarks of the NFL and the respective franchises; this is
an unofficial fan project.
