def totalCompra():
    total = 0

    while True:
        monton = float(input("Ingresa el monton de la compra: "))

        if monton == 0:
            break
        elif monton < 0:
            print("Monto negativo. Ingrese un nuevo monto.")
            continue

        total += monton

    if total > 1000:
        descuento = total * 0.10
        total -= descuento

    return total

def main():
    total = totalCompra()
    print(f"Total a pagar: {total:.2f}")

if __name__ == "__main__":
    main()
