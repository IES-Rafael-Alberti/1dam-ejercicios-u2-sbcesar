def mostrarCapital():
    amount = float(input("Introduce una cantidad a invertir: "))
    interest = int(input("Introduce el interes anual (%): "))
    years = int(input("Introduce los años: "))

    for year in range(1, years+1):
        amount *= 1 + interest / 100
        print(f"Año {year}: Capital obtenido  = {amount:.2f}")

    print(f"El capital final después de {years} años es {amount:.2f}")

def main():
    print(mostrarCapital())

if __name__ == "__main__":
    main()