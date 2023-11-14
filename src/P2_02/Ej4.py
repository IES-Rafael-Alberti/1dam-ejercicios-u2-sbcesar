def cuentaAtras():
    num = int(input("Introduce un numero entero positivo: "))
    for i in range(num, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end=", ")

def main():
    print(cuentaAtras())


if __name__ == "__main__":
    main()