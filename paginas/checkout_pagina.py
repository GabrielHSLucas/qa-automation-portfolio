from playwright.sync_api import Page


class CheckoutPagina:
    def __init__(self, page: Page):
        self.page = page
        self.campo_nome = page.locator('[data-test="firstName"]')
        self.campo_sobrenome = page.locator('[data-test="lastName"]')
        self.campo_cep = page.locator('[data-test="postalCode"]')
        self.botao_continuar = page.locator('[data-test="continue"]')
        self.botao_finalizar = page.locator('[data-test="finish"]')
        self.mensagem_erro = page.locator('[data-test="error"]')
        self.confirmacao = page.locator('[data-test="complete-header"]')

    def preencher_dados(self, nome, sobrenome, cep):
        self.campo_nome.fill(nome)
        self.campo_sobrenome.fill(sobrenome)
        self.campo_cep.fill(cep)
        self.botao_continuar.click()

    def finalizar(self):
        self.botao_finalizar.click()