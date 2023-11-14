nombre = input("Ingresa tu nombre: ")
sexo = input("Ingresa tu sexo (H/M): ")

nombre = nombre.upper()

if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre >= "M"):
    grupo = "A"
else:
    grupo = "B"

print(f"Tu nombre '{nombre}' te ubica en el grupo {grupo}.")
