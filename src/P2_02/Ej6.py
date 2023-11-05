def arbolito():
    num = int(input("Introduce un numero entero: "))
    caracter = "*"

    for i in range(1,num+1):
        print(caracter*i)

def main():
    arbolito()

if __name__ == "__main__":
    main()