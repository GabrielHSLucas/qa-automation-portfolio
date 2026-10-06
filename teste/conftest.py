import pytest
from api.cliente import criar_reserva, gerar_token


@pytest.fixture
def token():
    return gerar_token().json()["token"]


@pytest.fixture
def reserva_criada():
    return criar_reserva().json()["bookingid"]