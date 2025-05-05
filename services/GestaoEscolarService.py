import requests

BASE_URL = "https://gestao-escolar-api-3uu5.onrender.com/"

TOKEN_CACHE = {"token": None}

def get_token(): 
    if TOKEN_CACHE["token"]: 
        return TOKEN_CACHE["token"]


    if res.status_code == 200: 
        token = res.json()["access_token"]
        TOKEN_CACHE["token"] = token
        return token

    return None


def professor_existe(professor_id):

    token = get_token()
    if not token:
        return False
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f"{BASE_URL}/professores/{professor_id}", headers=headers)
    return res.status_code == 200

def turma_existe(turma_id):
    token = get_token()
    if not token: 
        return False
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.get(f'{BASE_URL}/turmas/{turma_id}', headers=headers)
    return res.status_code == 200

