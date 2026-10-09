from api.cliente import DADOS_RESERVA, apagar_reserva, atualizar_reserva, consultar_reserva, criar_reserva, gerar_token

import pytest


CASOS_LOGIN_API_INVALIDO = [
    ("admin", "senha-errada"),
    ("usuario_inexistente", "password123"),
    ("", "password123"),
    ("admin", ""),
]

IDS_LOGIN_API_INVALIDO = [
    "senha_errada",
    "usuario_inexistente",
    "usuario_vazio",
    "senha_vazia",
]

CAMPOS_OBRIGATORIOS = ["firstname", "lastname", "totalprice", "depositpaid", "bookingdates"]


def test_consultar_reserva_inexistente():
    assert consultar_reserva(999999999).status_code == 404


@pytest.mark.parametrize("usuario, senha", CASOS_LOGIN_API_INVALIDO, ids=IDS_LOGIN_API_INVALIDO)
def test_login_invalido_nao_gera_token(usuario, senha):
    resposta = gerar_token(usuario=usuario, senha=senha)
    assert "token" not in resposta.json()


def test_atualizar_reserva_sem_token_e_proibido(reserva_criada):
    resposta = atualizar_reserva(reserva_criada, DADOS_RESERVA)
    assert resposta.status_code == 403


def test_apagar_reserva_sem_token_e_proibido(reserva_criada):
    assert apagar_reserva(reserva_criada).status_code == 403


@pytest.mark.parametrize("campo", CAMPOS_OBRIGATORIOS)
def test_criar_reserva_sem_campo_obrigatorio_nao_e_aceita(campo):
    dados = {k: v for k, v in DADOS_RESERVA.items() if k != campo}
    resposta = criar_reserva(dados)
    assert resposta.status_code != 200


def test_criar_reserva_sem_campo_opcional_e_aceita():
    dados = {k: v for k, v in DADOS_RESERVA.items() if k != "additionalneeds"}
    resposta = criar_reserva(dados)
    assert resposta.status_code == 200


@pytest.mark.xfail(reason="API devolve 500; o esperado seria 400", strict=True)
@pytest.mark.parametrize("campo", CAMPOS_OBRIGATORIOS)
def test_criar_reserva_sem_campo_obrigatorio_retorna_400(campo):
    dados = {k: v for k, v in DADOS_RESERVA.items() if k != campo}
    resposta = criar_reserva(dados)
    assert resposta.status_code == 400