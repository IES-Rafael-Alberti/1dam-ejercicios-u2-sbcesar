def nVecesLetra(frase, letra):
    cont = 0
    for i in frase.lower():
        if i == letra:
            cont += 1
    print(f"La letra {letra} aparece en la frase {cont} veces.")

def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    nVecesLetra(frase, letra)

if __name__ == "__main__":
    main()