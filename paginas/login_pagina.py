from playwright.sync_api import Page


class LoginPagina:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page
        self.campo_usuario = page.locator('[data-test="username"]')
        self.campo_senha = page.locator('[data-test="password"]')
        self.botao_entrar = page.locator('[data-test="login-button"]')
        self.mensagem_erro = page.locator('[data-test="error"]')

    def abrir(self):
        self.page.goto(self.URL)

    def entrar(self, usuario, senha):
        self.campo_usuario.fill(usuario)
        self.campo_senha.fill(senha)
        self.botao_entrar.click()