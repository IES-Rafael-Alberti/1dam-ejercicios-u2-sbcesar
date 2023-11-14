def esPar(num):
    for i in range(1,num+1, 2):
        if i == num:
            print(i)
        else:
            print(i, end=", ")

def main():
    num = int(input("Introduce un numero entero positivo: "))
    esPar(num)


if __name__ == "__main__":
    main()