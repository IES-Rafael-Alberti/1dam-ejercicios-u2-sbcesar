def eco(entrada):
    return f"Eco: {entrada}"

def main():
    while True:
        entrada = input("Introduce una palabra: ")
        print(eco(entrada))

        if entrada == "salir":
            break

if __name__ == "__main__":
    main()