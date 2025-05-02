import requests

BASE_URL = "http://localhost:8080/api/v1/gestao-escolar"

def professor_existe(professor_id):
    res = requests.get(f'{BASE_URL}/professores/{professor_id}')
    return res.status_code == 200

def turma_existe(turma_id):
    res = requests.get(f'{BASE_URL}/turmas/{turma_id}')
    return res.status_code == 200

