import requests

base_url_api = "http://127.0.0.1:8000"

def do_get(route:str|None, params:dict|None = None):
    enpoint = base_url_api + route

    response = requests.get(url=enpoint, params=params)
    response.raise_for_status()

    return response.json()

def do_post(route:str|None, json:dict|None = None):
    endpoint = base_url_api + route

    response = requests.post(url=endpoint, json=json)
    response.raise_for_status()

    return response.json()