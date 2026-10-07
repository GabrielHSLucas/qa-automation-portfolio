from playwright.sync_api import expect

from paginas.login_pagina import LoginPagina
from paginas.produtos_pagina import ProdutosPagina


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


def test_login_com_senha_errada_mostra_erro(page):
    login = LoginPagina(page)
    login.abrir()
    login.entrar("standard_user", "senha-errada")
    expect(login.mensagem_erro).to_contain_text("do not match")


def test_usuario_bloqueado_nao_entra(page):
    login = LoginPagina(page)
    login.abrir()
    login.entrar("locked_out_user", "secret_sauce")
    expect(login.mensagem_erro).to_contain_text("locked out")