def contardorDigitos(numero):
    par = 0
    impar = 0

    while numero > 0:
        digito = numero % 10
        if digito % 2 == 0:
            par += 1
        else:
            impar += 1
        numero //= 10

    return par, impar

def main():
    totalPar = 0
    totalImpar = 0

    while True:
        num = int(input("Ingresa un número entero positivo: "))

        if num == 0:
            break
        elif num < 0:
            print("Número negativo. Ingresa un nuevo número positivo.")
            continue

        par, impar = contardorDigitos(num)
        totalPar += par
        totalImpar += impar

        print(f"Dígitos pares: {par}, Dígitos impares: {impar}")

    print(f"Total de dígitos pares leídos: {totalPar}")
    print(f"Total de dígitos impares leídos: {totalImpar}")

if __name__ == "__main__":
    main()