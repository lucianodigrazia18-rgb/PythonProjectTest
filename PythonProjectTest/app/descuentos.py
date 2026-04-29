def calcular_precio_final(monto):
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")

    if monto <= 100:
        return monto - (monto * 0.25)

    elif monto > 100:
        return monto - (monto * 0.50)

    return monto