from descuentos import calcular_precio_final

def main():
    monto = float(input("Ingrese el monto de la compra: "))
    precio_final = calcular_precio_final(monto)
    print(f"Precio final: ${precio_final:.2f}")

if __name__ == "__main__":
    main()

