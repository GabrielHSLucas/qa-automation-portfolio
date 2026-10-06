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


def gerar_token(usuario="admin", senha="password123"):
    return requests.post(f"{BASE_URL}/auth", json={"username": usuario, "password": senha})


def criar_reserva(dados=DADOS_RESERVA):
    return requests.post(f"{BASE_URL}/booking", json=dados, headers=CABECALHOS)


def consultar_reserva(id_reserva):
    return requests.get(f"{BASE_URL}/booking/{id_reserva}", headers=CABECALHOS)


def atualizar_reserva(id_reserva, dados, token=None):
    cabecalhos = dict(CABECALHOS)
    if token:
        cabecalhos["Cookie"] = f"token={token}"
    return requests.put(f"{BASE_URL}/booking/{id_reserva}", json=dados, headers=cabecalhos)


def apagar_reserva(id_reserva, token=None):
    cabecalhos = {"Cookie": f"token={token}"} if token else {}
    return requests.delete(f"{BASE_URL}/booking/{id_reserva}", headers=cabecalhos)