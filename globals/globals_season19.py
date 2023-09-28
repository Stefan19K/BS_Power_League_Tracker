SEASON = "season19"

MAX_NR_PLAYERS = 500
MAX_THREADS = 8
MAX_CONCURRENCY = 5

TOKEN = ""

HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}

# Rank related constants
BI = 1
MI = 13
LI = 16

# Url related constants
PLAYERS_URL = "https://api.brawlstars.com/v1/players/"
BATTLELOG_URL = "/battlelog"

# Excell related constants
FILE_PATH = "excell_data/season19_data.xlsx"
FILE_QUERY_PATH = "season19_data_query.xlsx"
TOTAL_GAMES = "A3"

MAPS = {
    "Hard Rock Mine"    : (2, 4),
    "Crystal Arcade"    : (8, 10),
    "Double Swoosh"     : (14, 16),
    "Shooting Star"     : (20, 22),
    "Canal Grande"      : (26, 28),
    "Infinite Doom"     : (32, 34),
    "Kaboom Canyon"     : (38, 40),
    "Pit Stop"          : (44, 46),
    "Safe Zone"         : (50, 52),
    "Pinhole Punt"      : (56, 58),
    "Pinball Dreams"    : (62, 64),
    "Field Goal"        : (68, 70),
    "Open Zone"         : (74, 76),
    "Ring of Fire"      : (80, 82),
    "Dueling Beetles"   : (86, 88),
    "Belle's Rock"      : (92, 94),
    "Flaring Phoenix"   : (98, 100),
    "Goldarm Gulch"     : (104, 106),
}

BRAWLERS = {
    "SHELLY" : 5,
    "NITA" : 6,
    "COLT" : 7,
    "BULL" : 8,
    "BROCK" : 9,
    "EL PRIMO" : 10,
    "BARLEY" : 11,
    "POCO" : 12,
    "ROSA" : 13,
    "JESSIE" : 14,
    "DYNAMIKE" : 15,
    "TICK" : 16,
    "8-BIT" : 17,
    "RICO" : 18,
    "DARRYL" : 19,
    "PENNY" : 20,
    "CARL" : 21,
    "JACKY" : 22,
    "GUS" : 23,
    "BO" : 24,
    "EMZ" : 25,
    "STU" : 26,
    "PIPER" : 27,
    "PAM" : 28,
    "FRANK" : 29,
    "BIBI" : 30,
    "BEA" : 31,
    "NANI" : 32,
    "EDGAR" : 33,
    "GRIFF" : 34,
    "GROM" : 35,
    "BONNIE" : 36,
    "HANK" : 37,
    "MORTIS" : 38,
    "TARA" : 39,
    "GENE" : 40,
    "MAX" : 41,
    "MR. P" : 42,
    "SPROUT" : 43,
    "BYRON" : 44,
    "SQUEAK" : 45,
    "GRAY" : 46,
    "WILLOW" : 47,
    "DOUG" : 48,
    "SPIKE" : 49,
    "CROW" : 50,
    "LEON" : 51,
    "SANDY" : 52,
    "AMBER" : 53,
    "MEG" : 54,
    "CHESTER" : 55,
    "GALE" : 56,
    "SURGE" : 57,
    "COLETTE" : 58,
    "LOU" : 59,
    "RUFFS" : 60,
    "BELLE" : 61,
    "BUZZ" : 62,
    "ASH" : 63,
    "LOLA" : 64,
    "FANG" : 65,
    "EVE" : 66,
    "JANET" : 67,
    "OTIS" : 68,
    "SAM" : 69,
    "BUSTER" : 70,
    "MANDY" : 71,
    "R-T" : 72,
    "MAISIE" : 73,
    "CORDELIUS" : 74
}