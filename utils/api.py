import requests

base_url_api = "http://127.0.0.1:8000"

def do_get(route:str|None, params:dict|None = None):
    try:
        enpoint = base_url_api + route
        response = requests.get(url=enpoint, params=params)
        return response.json(), None
    
    except requests.exceptions.HTTPError:
        return None, response.status_code()

    except requests.exceptions.RequestException:
        return None, "Erro de conexão"

def do_post(route:str|None, json:dict|None = None):
    try:
        endpoint = base_url_api + route
        response = requests.post(url=endpoint, json=json)
        return response.json(), None
    
    except requests.exceptions.HTTPError:
        return None, response.status_code()

    except requests.exceptions.RequestException:
        return None, "Erro de conexão"