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


def criar_reserva():
    resposta = requests.post(f"{BASE_URL}/booking", json=DADOS_RESERVA, headers=CABECALHOS)
    return resposta.json()["bookingid"]


def test_consultar_reserva_inexistente():
    resposta = requests.get(f"{BASE_URL}/booking/999999999", headers=CABECALHOS)
    assert resposta.status_code == 404


def test_login_com_senha_errada_nao_gera_token():
    credenciais = {"username": "admin", "password": "senha-errada"}
    resposta = requests.post(f"{BASE_URL}/auth", json=credenciais)
    assert "token" not in resposta.json()


def test_atualizar_reserva_sem_token_e_proibido():
    id_reserva = criar_reserva()
    resposta = requests.put(f"{BASE_URL}/booking/{id_reserva}", json=DADOS_RESERVA, headers=CABECALHOS)
    assert resposta.status_code == 403


def test_apagar_reserva_sem_token_e_proibido():
    id_reserva = criar_reserva()
    resposta = requests.delete(f"{BASE_URL}/booking/{id_reserva}")
    assert resposta.status_code == 403


def test_criar_reserva_sem_campos_obrigatorios_nao_e_aceita():
    dados_incompletos = {"firstname": "Gabriel"}
    resposta = requests.post(f"{BASE_URL}/booking", json=dados_incompletos, headers=CABECALHOS)
    assert resposta.status_code != 200