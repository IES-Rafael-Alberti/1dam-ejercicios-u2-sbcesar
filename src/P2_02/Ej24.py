from Ej10 import esPrimo

def main():
    cont = 0

    while True:
        num = int(input("Ingresa un número mayor que 1 (o 0 para finalizar): "))

        if num == 0:
            break
        elif num <= 1:
            print("Número inválido. Ingresa un número mayor que 1.")
            continue

        if esPrimo(num):
            cont += 1

    print(f"Números primos ingresados: {cont}")

if __name__ == "__main__":
    main()