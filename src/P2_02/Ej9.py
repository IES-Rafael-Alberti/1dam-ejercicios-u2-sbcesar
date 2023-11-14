def pedirContrasena(password):
    contrasena = "usuario"
    return password == contrasena

def main():
    while True:
        password = input("Introduce la contraseña: ")
        if pedirContrasena(password):
            print("La contraseña es correcta")
            break
        else:
            print("Introduzca la contraseña correcta")

if __name__ == "__main__":
    main()