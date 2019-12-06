import os
import json
from six.moves.urllib.request import urlopen, Request


def getSetting(setting):
    try:
        with open(os.path.dirname(__file__) + '/../../settings.json') as file:
            data = json.load(file)
            return data['settings'][setting]
    except FileNotFoundError:
        return None

def WinClient():
    pass
def UnixClient():
    pass


def getIcon(game):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    DEFAULT_ENCODING = 'utf-8'
    
    url = 'https://raw.githubusercontent.com/Chaottiic/StadiaCord/master/games.json'
    req = Request(url=url, headers=headers)
    urlResponse = urlopen(req).read()

    data = json.loads(urlResponse)
    for attrs in data:
        if attrs == game:
            if data[attrs]['assets'] == "":
                return "1"
            else:
                return data[attrs]['assets']

def getGameData(game):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    DEFAULT_ENCODING = 'utf-8'
    
    url = 'https://raw.githubusercontent.com/Chaottiic/StadiaCord/master/games.json'
    req = Request(url=url, headers=headers)
    urlResponse = urlopen(req).read()

    data = json.loads(urlResponse)
    for attrs in data:
        if attrs == game:
            return data[attrs]

def getGameID(game):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    DEFAULT_ENCODING = 'utf-8'
    
    url = 'https://raw.githubusercontent.com/Chaottiic/StadiaCord/master/games.json'
    req = Request(url=url, headers=headers)
    urlResponse = urlopen(req).read()

    data = json.loads(urlResponse)
    for attrs in data:
        if attrs == game:
            return data[attrs]["id"]

def getGameDataFromID(ID):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    DEFAULT_ENCODING = 'utf-8'
    
    url = 'https://raw.githubusercontent.com/Chaottiic/StadiaCord/master/games.json'
    req = Request(url=url, headers=headers)
    urlResponse = urlopen(req).read()

    data = json.loads(urlResponse)
    for attrs in data:
        if data[attrs]["id"] == ID:
            return data[attrs]

def getGameName(ID):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    DEFAULT_ENCODING = 'utf-8'
    
    url = 'https://raw.githubusercontent.com/Chaottiic/StadiaCord/master/games.json'
    req = Request(url=url, headers=headers)
    urlResponse = urlopen(req).read()

    data = json.loads(urlResponse)
    for attrs in data:
        if data[attrs]["id"] == ID:
            return attrs