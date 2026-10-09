from playwright.sync_api import expect

from paginas.login_pagina import LoginPagina
from paginas.produtos_pagina import ProdutosPagina

import pytest

CASOS_LOGIN_INVALIDO = [
    ("standard_user", "senha-errada", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("usuario_inexistente", "secret_sauce", "do not match"),
]

IDS_LOGIN_INVALIDO = [
    "senha_errada",
    "usuario_bloqueado",
    "usuario_vazio",
    "senha_vazia",
    "usuario_inexistente",
]


def test_pagina_de_login_carrega(page):
    login = LoginPagina(page)
    login.abrir()
    expect(page).to_have_title("Swag Labs")
    expect(login.botao_entrar).to_be_visible()


def test_login_valido_leva_aos_produtos(page):
    login = LoginPagina(page)
    login.abrir()
    login.entrar("standard_user", "secret_sauce")

    expect(page).to_have_url(f"{LoginPagina.URL}/inventory.html")
    expect(ProdutosPagina(page).itens).to_have_count(6)


@pytest.mark.parametrize("usuario, senha, mensagem", CASOS_LOGIN_INVALIDO, ids=IDS_LOGIN_INVALIDO)
def test_login_invalido_mostra_erro(page, usuario, senha, mensagem):
    login = LoginPagina(page)
    login.abrir()
    login.entrar(usuario, senha)
    expect(login.mensagem_erro).to_contain_text(mensagem)