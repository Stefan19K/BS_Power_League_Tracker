SEASON = "season21"

MAX_NR_PLAYERS = 96000
MAX_THREADS = 44
MAX_CONCURRENCY = 250

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjMzYWZlMmZjLWYwY2MtNGVjYy04NDdiLTg5OTZjM2JhYjcyZCIsImlhdCI6MTY5OTI4NTgxMSwic3ViIjoiZGV2ZWxvcGVyLzEwYzdhZTc0LTIxNTYtNmNmMC0xNzhjLTA4YTQwMTk3YTFlNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiODEuMTk2LjIxNS4zNyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.avVyUEED8ib5u1IzOscQ-Q-EttqCAzlWQPsvEpXEcHia4ozwIPYSz_pdne1VuMP1FfmtsTEi5rOHJWPukv65-A"

HEADERS = {'Authorization': 'Bearer {}'.format(TOKEN)}

# Rank related constants
BI = 1
MI = 13
LI = 16

# Url related constants
PLAYERS_URL = "https://api.brawlstars.com/v1/players/"
BATTLELOG_URL = "/battlelog"

# Git related constants
PATH_TO_GIT_REPO = ".git"
COMMIT_MESSAGE = "updated stats up to date"

# Excell related constants
FILE_PATH = "excell_data/season21_data.xlsx"
FILE_QUERY_PATH = "season21_data_query.xlsx"
TOTAL_GAMES = "A3"

MAPS = {
    "Hard Rock Mine"    : (2, 4),
    "Last Stop"         : (8, 10),
    "Double Swoosh"     : (14, 16),
    "Shooting Star"     : (20, 22),
    "Canal Grande"      : (26, 28),
    "Dry Season"        : (32, 34),
    "Kaboom Canyon"     : (38, 40),
    "Hot Potato"        : (44, 46),
    "Safe Zone"         : (50, 52),
    "Pinhole Punt"      : (56, 58),
    "Super Beach"       : (62, 64),
    "Field Goal"        : (68, 70),
    "Split"             : (74, 76),
    "Ring of Fire"      : (80, 82),
    "Dueling Beetles"   : (86, 88),
    "Belle's Rock"      : (92, 94),
    "Out in the Open"   : (98, 100),
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
    "CHUCK" : 49,
    "SPIKE" : 50,
    "CROW" : 51,
    "LEON" : 52,
    "SANDY" : 53,
    "AMBER" : 54,
    "MEG" : 55,
    "CHESTER" : 56,
    "GALE" : 57,
    "SURGE" : 58,
    "COLETTE" : 59,
    "LOU" : 60,
    "RUFFS" : 61,
    "BELLE" : 62,
    "BUZZ" : 63,
    "ASH" : 64,
    "LOLA" : 65,
    "FANG" : 66,
    "EVE" : 67,
    "JANET" : 68,
    "OTIS" : 69,
    "SAM" : 70,
    "BUSTER" : 71,
    "MANDY" : 72,
    "R-T" : 73,
    "MAISIE" : 74,
    "CORDELIUS" : 75,
    "PEARL" : 76,
    "CHARLIE" : 77
}