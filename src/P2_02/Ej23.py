def contarNumeros(linea):
    cont = 0
    for caracter in linea:
        if caracter in '0123456789':
            cont += 1
    return cont

def main():
    lineas = 0

    while True:
        libro = input("Libro: ")

        if libro == "*":
            break
        elif libro == "/":
            if lineas > 0:
                print(f"Aparecen {total_digitos} dígitos numéricos")
            else:
                print("No se encontraron dígitos numéricos")

            lineas += 1
            total_digitos = 0
        else:
            total_digitos += contarNumeros(libro)

    print(f"Se leyeron {lineas} líneas completas")

if __name__ == "__main__":
    main()