import pytest

from paginas.login_pagina import LoginPagina


@pytest.fixture
def pagina_logada(page):
    login = LoginPagina(page)
    login.abrir()
    login.entrar("standard_user", "secret_sauce")
    return page