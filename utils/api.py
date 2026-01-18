import requests

BASE_URL = "http://127.0.0.1:8000"

def librion_api(method: str,route: str, *,params=None,json=None,data=None,headers=None,timeout=10):
    url = BASE_URL + route

    # monta apenas o que não é None
    kwargs = {
        "params": params,
        "json": json,
        "data": data,
        "headers": headers,
        "timeout": timeout
    }

    # remove os None
    kwargs = {k: v for k, v in kwargs.items() if v is not None}

    try:
        response = requests.request(method, url, **kwargs)

        # Sucesso
        if 200 <= response.status_code < 300:
            return {
                "success": True,
                "data": response.json(),
                "status": response.status_code
            }
        # Erro na API
        return {
            "success": False,
            "error": response.json(),
            "status": response.status_code
        }

    # Erro de conexão
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "status": None
        }



def do_get(route:str|None, params:dict|None = None, headers:dict|None = None):
    try:
        enpoint = BASE_URL + route
        response = requests.get(url=enpoint, params=params, headers=headers)

        # Sucesso
        if 200 <= response.status_code < 300:
            return {
                "sucess": True,
                "data": response.json(),
                "status": response.status_code
            }

        # Erro na API
        return {
            "sucess": False,
            "data": response.json(),
            "status": response.status_code
        }

    # Erro na requisição (requests)
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "status": None
        }

def do_post(route:str|None, json:dict|None = None):
    try:
        endpoint = BASE_URL + route
        response = requests.post(url=endpoint, json=json)
        return response.json(), None
    
    except requests.exceptions.HTTPError:
        return None, response.status_code()

    except requests.exceptions.RequestException:
        return None, "Erro de conexão"