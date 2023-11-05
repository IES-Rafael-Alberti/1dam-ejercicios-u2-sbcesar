def comenzar():
    print("Hola")
    print()

def imprimir():
    print("Lista :D")
    print()

def main():
    while True:
        opcion = input("Menú:\n 1 - Comenzar programa\n 2 - Imprimir listado\n 3 - Finalizar programa\n")

        if opcion == "1":
            comenzar()
        elif opcion == "2":
            imprimir()
        elif opcion == "3":
            print("Finalizando el programa.")
            break
        else:
            print("Opción incorrecta. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
