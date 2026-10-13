import pytest

pytestmark = pytest.mark.dados


def test_documentos_dos_clientes_nao_se_repetem(banco):
    duplicados = banco.execute(
        "SELECT documento, COUNT(*) FROM clientes GROUP BY documento HAVING COUNT(*) > 1"
    ).fetchall()
    assert duplicados == []


def test_todo_contrato_pertence_a_um_cliente_existente(banco):
    orfaos = banco.execute(
        """
        SELECT c.id FROM contratos c
        LEFT JOIN clientes cl ON cl.id = c.cliente_id
        WHERE cl.id IS NULL
        """
    ).fetchall()
    assert orfaos == []


def test_valor_total_e_igual_a_parcelas_vezes_valor_da_parcela(banco):
    divergentes = banco.execute(
        "SELECT id FROM contratos WHERE ROUND(numero_parcelas * valor_parcela, 2) != ROUND(valor_total, 2)"
    ).fetchall()
    assert divergentes == []


def test_nenhum_contrato_tem_valor_ou_parcelas_invalidos(banco):
    invalidos = banco.execute(
        "SELECT id FROM contratos WHERE valor_total <= 0 OR numero_parcelas <= 0 OR valor_parcela <= 0"
    ).fetchall()
    assert invalidos == []


def test_nenhum_cliente_tem_nome_vazio(banco):
    vazios = banco.execute(
        "SELECT id FROM clientes WHERE nome = ''"
    ).fetchall()
    assert vazios == []