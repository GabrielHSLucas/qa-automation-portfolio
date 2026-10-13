import sqlite3
import pytest


@pytest.fixture(scope="module")
def banco():
    conexao = sqlite3.connect(":memory:")
    cursor = conexao.cursor()

    cursor.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            documento TEXT NOT NULL
        );
        CREATE TABLE contratos (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER NOT NULL,
            valor_total REAL NOT NULL,
            numero_parcelas INTEGER NOT NULL,
            valor_parcela REAL NOT NULL
        );
    """)

    cursor.executemany(
        "INSERT INTO clientes (id, nome, documento) VALUES (?, ?, ?)",
        [
            (1, "Cliente Um", "000.000.000-01"),
            (2, "Cliente Dois", "000.000.000-02"),
            (3, "Cliente Tres", "000.000.000-03"),
        ],
    )
    cursor.executemany(
        "INSERT INTO contratos (id, cliente_id, valor_total, numero_parcelas, valor_parcela) VALUES (?, ?, ?, ?, ?)",
        [
            (1, 1, 1200.00, 12, 100.00),
            (2, 1, 600.00, 6, 100.00),
            (3, 2, 2400.00, 24, 100.00),
            (4, 3, 500.00, 5, 100.00),
            
        ],
    )
    conexao.commit()

    yield conexao
    conexao.close()