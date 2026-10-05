import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"
CABECALHOS = {"Content-Type": "application/json", "Accept": "application/json"}

DADOS_RESERVA = {
    "firstname": "Gabriel",
    "lastname": "Teste",
    "totalprice": 150,
    "depositpaid": True,
    "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
    "additionalneeds": "Café da manhã",
}


@pytest.fixture
def token():
    credenciais = {"username": "admin", "password": "password123"}
    resposta = requests.post(f"{BASE_URL}/auth", json=credenciais)
    return resposta.json()["token"]


@pytest.fixture
def reserva_criada():
    resposta = requests.post(f"{BASE_URL}/booking", json=DADOS_RESERVA, headers=CABECALHOS)
    return resposta.json()["bookingid"]


def test_criar_reserva():
    resposta = requests.post(f"{BASE_URL}/booking", json=DADOS_RESERVA, headers=CABECALHOS)
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert "bookingid" in corpo
    assert corpo["booking"]["firstname"] == "Gabriel"


def test_consultar_reserva(reserva_criada):
    resposta = requests.get(f"{BASE_URL}/booking/{reserva_criada}", headers=CABECALHOS)
    assert resposta.status_code == 200
    assert resposta.json()["lastname"] == "Teste"


def test_atualizar_reserva(reserva_criada, token):
    novos_dados = {**DADOS_RESERVA, "firstname": "Gabriel Lucas"}
    cabecalhos = {**CABECALHOS, "Cookie": f"token={token}"}
    resposta = requests.put(f"{BASE_URL}/booking/{reserva_criada}", json=novos_dados, headers=cabecalhos)
    assert resposta.status_code == 200
    assert resposta.json()["firstname"] == "Gabriel Lucas"


def test_apagar_reserva(reserva_criada, token):
    cabecalhos = {"Cookie": f"token={token}"}
    resposta = requests.delete(f"{BASE_URL}/booking/{reserva_criada}", headers=cabecalhos)
    assert resposta.status_code == 201

    consulta = requests.get(f"{BASE_URL}/booking/{reserva_criada}", headers=CABECALHOS)
    assert consulta.status_code == 404