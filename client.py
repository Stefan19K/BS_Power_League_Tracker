import requests as req
import json
from globals.globals_season20 import *

class Result:
    def __init__(self, val=None, err=None):
        self.val = val
        self.err = err

class Client:
    headers = {'Authorization': 'Bearer {}'.format(TOKEN)}

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def get_player_battlelog(tag: str) -> dict:
        f_tag = convert_id_to_fetchable_id(tag)
        url = PLAYERS_URL + f_tag + BATTLELOG_URL
        try:
            res = req.get(url=url, headers=Client.headers)
        except req.exceptions.RequestException as error:
            print("Couldn't retrieve battlelog for player with tag {}. Error : {}".format(tag, error))
            return None

        if res.status_code == 200:
            json_object = json.loads(res.content)
            return json_object
        else:
            print("Couldn't retrieve battlelog for player with tag {}. Error : {}".format(tag, res.reason))
            return None

def convert_id_to_fetchable_id(id: str):
    if id[0] == '#' or id[0:2] != "%23":
        return "%23" + id[1:]
    
    return id    
    # add more code here to treat possible cases
