from calculator import sumar, restar, multiplicar, dividir


def main():
    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Hasta pronto.")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida.")
            continue

        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))

            if opcion == "1":
                resultado = sumar(a, b)
            elif opcion == "2":
                resultado = restar(a, b)
            elif opcion == "3":
                resultado = multiplicar(a, b)
            else:
                resultado = dividir(a, b)

            print(f"Resultado: {resultado}")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()