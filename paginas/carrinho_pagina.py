from playwright.sync_api import Page


class CarrinhoPagina:
    def __init__(self, page: Page):
        self.page = page
        self.nomes_dos_produtos = page.locator('[data-test="inventory-item-name"]')
        self.botao_checkout = page.locator('[data-test="checkout"]')

    def iniciar_checkout(self):
        self.botao_checkout.click()