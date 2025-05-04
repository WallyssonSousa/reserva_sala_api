import requests

BASE_URL = "https://gestao-escolar-api-3uu5.onrender.com/"

""" e4340d5ce26ec43f2274105cc4a6dd67 -> senha admin """

def professor_existe(professor_id):
    res = requests.get(f'{BASE_URL}/professores/{professor_id}')
    return res.status_code == 200

def turma_existe(turma_id):
    res = requests.get(f'{BASE_URL}/turmas/{turma_id}')
    return res.status_code == 200

