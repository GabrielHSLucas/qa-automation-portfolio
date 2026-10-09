# QA Automation Portfolio

![Testes](https://github.com/GabrielHSLucas/qa-automation-portfolio/actions/workflows/testes.yml/badge.svg)

Projeto de automação de testes em Python que cobre duas camadas, **API** e **interface web**,
com execução automática a cada alteração via GitHub Actions.

## Tecnologias

Python · pytest · requests · Playwright · pytest-html · GitHub Actions

## O que é testado

**API** ([Restful-Booker](https://restful-booker.herokuapp.com))
- Criar, consultar, atualizar e apagar reservas
- Casos negativos: reserva inexistente, login com senha errada, alteração e exclusão sem token, dados incompletos

**Interface** ([SauceDemo](https://www.saucedemo.com))
- Login válido, senha errada e usuário bloqueado
- Adicionar e remover produto do carrinho
- Compra completa e erro no checkout com dados obrigatórios ausentes

## Estrutura

```
api/                    cliente que centraliza as chamadas à API
paginas/                Page Objects (uma classe por tela do site)
teste/                  testes de API
teste/ui/               testes de interface e fixture de login
.github/workflows/      pipeline que roda tudo a cada push
pytest.ini              configuração do pytest
requirements.txt        dependências do projeto
```

## Decisões do projeto

- **Cliente de API separado dos testes:** as chamadas ficam em `api/cliente.py`, então uma mudança na API se corrige em um lugar só.
- **Page Object:** os elementos e as ações de cada tela ficam em `paginas/`, e a conferência (`expect`) fica no teste.
- **Fixtures:** a preparação (token, reserva, login) fica em `conftest.py` e não se repete nos testes.
- **Mais testes de API que de interface:** a API é mais rápida e estável, e a interface cobre só os fluxos principais.
- **Testes parametrizados:** cenários que só mudam os dados (logins inválidos, campos obrigatórios) usam `parametrize`, com uma tabela de casos e um único roteiro de teste.

## Como rodar

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest -v
```

No Mac ou Linux, ative o ambiente com `source .venv/bin/activate`.

Para ver o navegador durante os testes de interface:

```
pytest teste/ui --headed --slowmo 700
```

Para gerar o relatório em HTML:

```
pytest -v --html=relatorio.html --self-contained-html
```

## Pipeline

A cada push na `main`, o GitHub Actions instala as dependências e o navegador, roda todos os
testes e guarda o relatório HTML como artefato da execução (aba **Actions**, seção **Artifacts**).

## Próximos passos

- Mais cenários de interface (ordenação de produtos, carrinho com vários itens)
- Seção de observações com o que foi descoberto ao testar as APIs

## Observações

- Ao criar uma reserva sem um campo obrigatório (`firstname`, `lastname`, `totalprice`, `depositpaid` ou `bookingdates`), a API devolve **500 (erro interno do servidor)**. O esperado seria 400 (requisição inválida). Os testes conferem apenas que a reserva não é aceita.
- O campo `additionalneeds` é opcional: a reserva é criada normalmente sem ele.