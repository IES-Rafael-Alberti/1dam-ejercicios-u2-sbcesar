edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))

if edad > 16 and ingresos > 1000.0:
    print("Tributas")
else:
    print("No tributas")