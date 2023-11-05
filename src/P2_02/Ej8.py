def trianguloImpar(num):
    for i in range(0, num + 1):
        for j in range(2 * i -1, 0, -2):
            print(j, end=" ")
        print()
            
            

def main():
    num = int(input("Introduce un numero entero: "))
    trianguloImpar(num)

if __name__ == "__main__":
    main()