
import math
import pytest
from loja.voucher import validar_voucher

@pytest.mark.parametrize("valor", [
    50.0,                  # limite inferior inclusivo
    75.0,                  # dentro do intervalo
    500.0,                 # limite superior inclusivo
    50.1,                  # ligeiramente acima do limite inferior
    499.9,           # ligeiramente abaixo do limite superior
])
def test_valores_validos(valor):
    assert validar_voucher(valor) is True

@pytest.mark.parametrize("valor", [
    49.9,                  # ligeiramente abaixo do limite inferior
    0.0,                   # bem abaixo
    -10.0,                 # negativo
    500.1,                 # ligeiramente acima do limite superior
    1_000_000.0,           # muito acima
])
def test_valores_invalidos(valor):
    assert validar_voucher(valor) is False
