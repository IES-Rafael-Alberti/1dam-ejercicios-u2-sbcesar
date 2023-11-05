def tablasMultiplicar(tabla):
    for i in range(1,11):
        multiplicacion = tabla * i
        print(f"{tabla} x {i} = {multiplicacion}")

def main():
    tabla = int(input("Introduce la tabla de multiplicar que deseas ver (1-10): "))
    tablasMultiplicar(tabla)

if __name__ == "__main__":
    main()