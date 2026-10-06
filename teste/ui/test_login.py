from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com"


def test_pagina_de_login_carrega(page: Page):
    page.goto(URL)
    expect(page).to_have_title("Swag Labs")
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_login_valido_leva_aos_produtos(page: Page):
    page.goto(URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(f"{URL}/inventory.html")
    expect(page.locator('[data-test="inventory-item"]')).to_have_count(6)


def test_login_com_senha_errada_mostra_erro(page: Page):
    page.goto(URL)
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("senha-errada")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_contain_text("do not match")


def test_usuario_bloqueado_nao_entra(page: Page):
    page.goto(URL)
    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_contain_text("locked out")