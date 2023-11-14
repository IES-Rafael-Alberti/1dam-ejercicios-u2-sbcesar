opcion = int(input("Elige una opción:\n 1. Vegetariano\n 2. No Vegetariano\n 3. Salir\n"))
fijos = "mozzarella y el tomate"

while opcion:
    if opcion == 1:
        opcion = "vegetariana"
        ingrediente = int(input("Elige un ingrediente:\n 1. Pimiento\n 2. Tofu\n"))
        if ingrediente == 1:
            ingrediente = "pimiento"
        elif ingrediente == 2:
            ingrediente = "Tofu"
        else:
            print("Error - Por favor, introduzca una opción disponible")
        print(f"Tu pizza {opcion} contiene {ingrediente} obviando la {fijos}")
        break
    elif opcion == 2:
        opcion = "no vegetariana"
        ingrediente = int(input("Elige un ingrediente:\n 1. peperoni\n 2. jamón\n 3. salmón\n"))
        if ingrediente == 1:
            ingrediente = "peperoni"
        elif ingrediente == 2:
            ingrediente = "jamón"
        elif ingrediente == 3:
            ingrediente = "salmón"
        else:
            print("Error - Por favor, introduzca una opción disponible")
        print(f"Tu pizza {opcion} contiene {ingrediente} obviando la {fijos}")
        break
    elif opcion == 3:
        break
    else:
        print("Error - Por favor, introduzca una opción disponible")
        break