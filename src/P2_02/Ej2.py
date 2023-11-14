def pedirEdad():
    edad = int(input("Introduce tu edad: "))
    for i in range(0,edad+1):
        print(i, end=" ")

def main():
    print(pedirEdad())

if __name__ == "__main__":
    main()