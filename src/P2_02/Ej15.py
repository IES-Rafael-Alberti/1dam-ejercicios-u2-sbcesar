def sumatoriaPositivos(num):
    cont = 0

    while num != 0:
        if num > 0:
            cont += num
        num = int(input("Introduce otro numero: "))
        if num == 0:
            break
    
    return cont

def main():
    total = 0
    while True:
        num = int(input("Introduce un numero: "))
        if num < 0: #Ignora si el numero es negativo
            continue
        total += sumatoriaPositivos(num)
        print(total)
        break
    

if __name__ == "__main__":
    main()