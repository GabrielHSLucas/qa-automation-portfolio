from playwright.sync_api import Page


class ProdutosPagina:
    def __init__(self, page: Page):
        self.page = page
        self.itens = page.locator('[data-test="inventory-item"]')
        self.contador_carrinho = page.locator('[data-test="shopping-cart-badge"]')
        self.icone_carrinho = page.locator('[data-test="shopping-cart-link"]')

    def adicionar(self, produto):
        self.page.locator(f'[data-test="add-to-cart-{produto}"]').click()

    def abrir_carrinho(self):
        self.icone_carrinho.click()