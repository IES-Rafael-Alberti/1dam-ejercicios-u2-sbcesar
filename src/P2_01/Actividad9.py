edad = int(input("Introduce tu edad: "))

while edad > 0:
    if edad < 4:
        print("Entrada gratis")
    elif edad >= 4 and edad < 18:
        print("La entrada cuesta 5€")
    else:
        print("La entrada cuesta 10€")
    break
else:
    print("Error - Introduce una edad real")