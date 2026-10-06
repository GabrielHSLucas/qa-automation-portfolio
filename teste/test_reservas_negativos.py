from api.cliente import DADOS_RESERVA, apagar_reserva, atualizar_reserva, consultar_reserva, criar_reserva, gerar_token


def test_consultar_reserva_inexistente():
    assert consultar_reserva(999999999).status_code == 404


def test_login_com_senha_errada_nao_gera_token():
    resposta = gerar_token(senha="senha-errada")
    assert "token" not in resposta.json()


def test_atualizar_reserva_sem_token_e_proibido(reserva_criada):
    resposta = atualizar_reserva(reserva_criada, DADOS_RESERVA)
    assert resposta.status_code == 403


def test_apagar_reserva_sem_token_e_proibido(reserva_criada):
    assert apagar_reserva(reserva_criada).status_code == 403


def test_criar_reserva_sem_campos_obrigatorios_nao_e_aceita():
    resposta = criar_reserva({"firstname": "Gabriel"})
    assert resposta.status_code != 200