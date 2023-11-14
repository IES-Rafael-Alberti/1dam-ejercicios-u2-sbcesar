def encontrar():
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")
    encontrado = False

    for i in range(len(frase)):
        if frase[i] == letra:
            print(f"La letra '{letra}' se encontró en la posición {i}.")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró la letra '{letra}' en la frase.")

def main():
    encontrar()

if __name__ == "__main__":
    main()
