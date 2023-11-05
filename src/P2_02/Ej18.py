from Ej17 import sumaDigitos

def main():
    cont = 0
    while True:
        num = int(input("Introduce un número entero positivo: "))
        
        if num == -1:
            break

        if num < 0:
            print("El número ingresado no es positivo.")
            continue

        if num % 2 == 0:
            cont += 1

        suma = sumaDigitos(num)
        print(f"Suma: {suma}")
        
    print(f"Cantidad de numero pares: {cont}")

if __name__ == "__main__":
    main()