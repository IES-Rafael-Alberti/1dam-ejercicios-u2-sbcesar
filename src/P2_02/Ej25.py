def palabraMasLarga(frase):
    palabra = ""
    palabraLarga = ""
    longPalabra = 0
    longMax = 0

    for letra in frase:
        if letra != " ":
            palabra += letra
            longPalabra += 1
        else:
            if longPalabra > longMax:
                palabraLarga = palabra
                longMax = longPalabra
            palabra = ""
            longPalabra = 0

    if longPalabra > longMax:
        palabraLarga = palabra

    return palabraLarga

def main():
    frase = input("Ingresa una frase: ")
    palabraLarga = palabraMasLarga(frase)

    if palabraLarga:
        print(f"La palabra más larga es: {palabraLarga}")
    else:
        print("No se ingresaron palabras.")

    palabras = frase.split()
    cantidad_palabras = len(palabras)
    print(f"Cantidad de palabras en la frase: {cantidad_palabras}")

if __name__ == "__main__":
    main()