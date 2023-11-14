def numMayor():
    mayor = -1
    while True:
        num = int(input("Introduce un numero entero positivo: "))
        if num == 0:
            break
        if num > mayor:
            mayor = num
    return mayor

def main():
    print(numMayor())

if __name__ == "__main__":
    main()