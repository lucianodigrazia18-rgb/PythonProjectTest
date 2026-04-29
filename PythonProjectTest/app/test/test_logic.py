import pytest
from app.descuentos import calcular_precio_final


def test_descuento_10_por_ciento():
    resultado = calcular_precio_final(100)
    assert resultado == 75


def test_monto_negativo_error():
    with pytest.raises(ValueError):
        calcular_precio_final(-100)


def test_caso_borde_descuento_20_por_ciento():
    resultado = calcular_precio_final(200)
    assert resultado == 100