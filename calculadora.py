
def calculadora():
    print("===  CALCULADORA DE EXPRESIONES ===")
    print("Escribe una expresión matemática (por ejemplo: 3 + 5 * (2 - 1))")
    print("Escribe 'salir' para terminar.\n")

    while True:
        expresion = input("➡ Ingresa una expresión: ")

        if expresion.lower() == "salir":
            print(" ¡Hasta luego!")
            break

        try:

            resultado = eval(expresion, {"__builtins__": None}, {})
            print(f" Resultado: {resultado}\n")

        except ZeroDivisionError:
            print(" Error: No se puede dividir entre cero.\n")

        except (SyntaxError, NameError):
            print(" Error: La expresión no es válida.\n")

        except Exception as e:
            print(f" Ocurrió un error inesperado: {e}\n")


# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()