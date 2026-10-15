import json
from pathlib import Path

import pytest

from assistente.bot import responder

pytestmark = pytest.mark.ia

CASOS = json.loads((Path(__file__).parent / "casos.json").read_text(encoding="utf-8"))


def _preparar(caso):
    marcas = []
    if caso.get("falha_conhecida"):
        marcas.append(pytest.mark.xfail(reason=caso["falha_conhecida"], strict=True))
    return pytest.param(caso, marks=marcas, id=caso["id"])


@pytest.mark.parametrize("caso", [_preparar(c) for c in CASOS])
def test_resposta_do_assistente(caso):
    resposta = responder(caso["pergunta"]).lower()

    for trecho in caso["deve_conter"]:
        assert trecho.lower() in resposta

    for trecho in caso["nao_deve_conter"]:
        assert trecho.lower() not in resposta