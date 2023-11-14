def esPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

def main():
    num = int(input("Introduce un numero entero: "))
    esPrimo(num)

if __name__ == "__main__":
    main()