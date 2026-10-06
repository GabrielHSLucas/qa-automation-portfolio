from api.cliente import DADOS_RESERVA, apagar_reserva, atualizar_reserva, consultar_reserva, criar_reserva


def test_criar_reserva():
    resposta = criar_reserva()
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert "bookingid" in corpo
    assert corpo["booking"]["firstname"] == "Gabriel"


def test_consultar_reserva(reserva_criada):
    resposta = consultar_reserva(reserva_criada)
    assert resposta.status_code == 200
    assert resposta.json()["lastname"] == "Teste"


def test_atualizar_reserva(reserva_criada, token):
    novos_dados = {**DADOS_RESERVA, "firstname": "Gabriel Lucas"}
    resposta = atualizar_reserva(reserva_criada, novos_dados, token)
    assert resposta.status_code == 200
    assert resposta.json()["firstname"] == "Gabriel Lucas"


def test_apagar_reserva(reserva_criada, token):
    resposta = apagar_reserva(reserva_criada, token)
    assert resposta.status_code == 201
    assert consultar_reserva(reserva_criada).status_code == 404