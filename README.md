# BS_Power_League_Tracker

This is a basic mini-project that allows you to to track Power League stats
from Brawl Stars(currently the winrate and playrate for the top 15 brawlers
on each map, also categorized on the Power League rankings).

What does this project contain?
    - "file copies" folder only used localy in case the main files get corrupted.
    - "gamemodes" folder in which a configuration is set of the current Power
League rotation based on the current season.
    - "globals" folder contains all the globals used in the scripts. For each
season that passes a new globals file will be generated to match the current
season.
    - "maps" folder that contains all of the maps in the current rotation.
    - "pictures" folder that contains all of the png's used by the stats_query.py
script.
    - "client.py" library that contains a Client class to make requests easier.
    - "stats.py" and "stats_query.py" main scripts.
    - "player_tags" file that contains all of the players tags to be processed.
    - "requirements.txt" file that contains the packages to be installed in order
to be able to run the scripts.

Stats.py:
    This is the script where the data collection happens. This script runs
infinitely, passing sequentially through each player tag and making GET requests
the the BrawlStars API. New Power League battles are saved and then written in
the excell file featuring the current season.

Stats_query.py:
    This is the script that represents a simple GUI for the excell file in order
to make understanding the data much easier.

Updates:
- Version 1.0.1:
  - Now the app automatically adds new players to the dataset. Max players that
    can be registered : 500.

- Version 1.0.0:
  - Added sequential traversal of players stored locally to retrieve battles and
    save the data to a local excell file.
  - Added a GUI to make reading data fro mthe excell file much easier and
    user-friendly.
