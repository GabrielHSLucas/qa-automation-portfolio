from playwright.sync_api import expect

from paginas.carrinho_pagina import CarrinhoPagina
from paginas.checkout_pagina import CheckoutPagina
from paginas.produtos_pagina import ProdutosPagina

import pytest


PRODUTO = "sauce-labs-backpack"
NOME_DO_PRODUTO = "Sauce Labs Backpack"

CASOS_CHECKOUT_INVALIDO = [
    ("", "Lucas", "00000-000", "First Name is required"),
    ("Gabriel", "", "00000-000", "Last Name is required"),
    ("Gabriel", "Lucas", "", "Postal Code is required"),
]

IDS_CHECKOUT_INVALIDO = [
    "first_name_required",
    "last_name_required",
    "postal_code_required",
]


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

@pytest.mark.parametrize("nome, sobrenome, cep, mensagem", CASOS_CHECKOUT_INVALIDO, ids=IDS_CHECKOUT_INVALIDO)
def test_checkout_com_campo_obrigatorio_vazio_mostra_erros(pagina_logada, nome, sobrenome, cep, mensagem):
    produtos = ProdutosPagina(pagina_logada)
    produtos.adicionar(PRODUTO)
    produtos.abrir_carrinho()
    CarrinhoPagina(pagina_logada).iniciar_checkout()

    checkout = CheckoutPagina(pagina_logada)
    checkout.preencher_dados(nome, sobrenome, cep)

    expect(checkout.mensagem_erro).to_contain_text(mensagem)

def test_remover_produto_do_carrinho(pagina_logada):
    produtos = ProdutosPagina(pagina_logada)
    produtos.adicionar(PRODUTO)
    produtos.abrir_carrinho()

    carrinho = CarrinhoPagina(pagina_logada)
    expect(carrinho.nomes_dos_produtos).to_have_text([NOME_DO_PRODUTO])

    carrinho.remover_produto(PRODUTO)

    expect(carrinho.nomes_dos_produtos).to_have_count(0)

