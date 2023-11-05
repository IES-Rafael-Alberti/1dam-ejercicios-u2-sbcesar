def sumaDigitos(num):
    cont = 0
    while num > 0:
        digito = num % 10
        cont += digito
        num //= 10
    return cont

def main():
    num = int(input("Introduce un numero entero positivo: "))
    if num < 0:
        print("El número ingresado no es positivo.")
    else:
        print(sumaDigitos(num))
        

if __name__ == "__main__":
    main()