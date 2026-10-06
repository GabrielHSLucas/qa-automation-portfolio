import requests
from api.cliente import BASE_URL


def test_servico_esta_no_ar():
    resposta = requests.get(f"{BASE_URL}/ping")
    assert resposta.status_code == 201


def test_lista_de_reservas_retorna_lista():
    resposta = requests.get(f"{BASE_URL}/booking")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)