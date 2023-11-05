def palabraAlReves(palabra):
    palabraInvertida = ""
    for letra in palabra:
        palabraInvertida = letra + palabraInvertida
    return palabraInvertida

def main():
    palabra = input("Introduce una palabra: ")
    print(f"Palabra invertida: {palabraAlReves(palabra)}")

if __name__ == "__main__":
    main()

#También puedo hacerlo así

"""
def palabraAlReves(palabra):
    return palabra[::-1]
"""