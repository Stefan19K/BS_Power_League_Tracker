import requests as req
import json
from globals.globals_season20 import *

class Client:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': 'Bearer {}'.format(token)}
        self.battlelog = {}

    def get_player_battlelog(self, tag):
        url = PLAYERS_URL + tag + BATTLELOG_URL
        try:
            res = req.get(url=url, headers=self.headers)
        except req.exceptions.RequestException as _:
            return None

        if res.status_code == 200:
            json_object = json.loads(res.content)
            return json_object
        else:
            return None
