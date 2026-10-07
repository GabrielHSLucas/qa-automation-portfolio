from playwright.sync_api import expect

from paginas.carrinho_pagina import CarrinhoPagina
from paginas.checkout_pagina import CheckoutPagina
from paginas.produtos_pagina import ProdutosPagina

PRODUTO = "sauce-labs-backpack"
NOME_DO_PRODUTO = "Sauce Labs Backpack"


def test_adicionar_produto_atualiza_contador_do_carrinho(pagina_logada):
    produtos = ProdutosPagina(pagina_logada)
    produtos.adicionar(PRODUTO)
    expect(produtos.contador_carrinho).to_have_text("1")


def test_produto_adicionado_aparece_no_carrinho(pagina_logada):
    produtos = ProdutosPagina(pagina_logada)
    produtos.adicionar(PRODUTO)
    produtos.abrir_carrinho()

    carrinho = CarrinhoPagina(pagina_logada)
    expect(carrinho.nomes_dos_produtos).to_have_text([NOME_DO_PRODUTO])


def test_compra_completa_mostra_confirmacao(pagina_logada):
    produtos = ProdutosPagina(pagina_logada)
    produtos.adicionar(PRODUTO)
    produtos.abrir_carrinho()
    CarrinhoPagina(pagina_logada).iniciar_checkout()

    checkout = CheckoutPagina(pagina_logada)
    checkout.preencher_dados("Gabriel", "Lucas", "01000-000")
    checkout.finalizar()

    expect(checkout.confirmacao).to_have_text("Thank you for your order!")


def test_checkout_sem_nome_mostra_erro(pagina_logada):
    produtos = ProdutosPagina(pagina_logada)
    produtos.adicionar(PRODUTO)
    produtos.abrir_carrinho()
    CarrinhoPagina(pagina_logada).iniciar_checkout()

    checkout = CheckoutPagina(pagina_logada)
    checkout.preencher_dados("", "Lucas", "01000-000")

    expect(checkout.mensagem_erro).to_contain_text("First Name is required")