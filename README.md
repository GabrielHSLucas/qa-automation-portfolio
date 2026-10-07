# QA Automation Portfolio

![Testes](https://github.com/GabrielHSLucas/qa-automation-portfolio/actions/workflows/testes.yml/badge.svg)

Projeto de automação de testes em Python que cobre duas camadas: **API** e **interface web**,
com execução automática a cada alteração via GitHub Actions.

## Tecnologias

Python · pytest · requests · Playwright · GitHub Actions

## O que é testado

- **API** ([Restful-Booker](https://restful-booker.herokuapp.com)): criar, consultar, atualizar e apagar reservas, mais casos negativos (sem token, dados incompletos, reserva inexistente)
- **Interface** ([SauceDemo](https://www.saucedemo.com)): login válido e inválido, usuário bloqueado, carrinho e compra completa, incluindo erro no checkout

## Estrutura

- `api/`: cliente que centraliza as chamadas à API
- `paginas/`: Page Objects (uma classe por tela do site)
- `teste/`: testes de API e de interface
- `.github/workflows/`: pipeline que roda tudo a cada push

## Como rodar

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest -v
```

No Mac ou Linux, ative o ambiente com `source .venv/bin/activate`.
Para ver o navegador durante os testes de interface: `pytest teste/ui --headed --slowmo 700`.

## Pipeline

A cada push na `main`, o GitHub Actions instala as dependências, roda todos os testes
e guarda o relatório de resultados como artefato da execução.

## Próximos passos

- Relatório de testes em HTML
- Mais cenários de interface (ordenação e remoção de produtos)