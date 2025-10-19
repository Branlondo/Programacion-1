def calculadora_cientifica(operacion, a, b):
    """
    Realiza operaciones matemáticas básicas entre dos números.

    Parámetros:
    - operacion (str): Tipo de operación a realizar. Debe ser una de: suma, resta, multiplicacion, division, potencia, modulo.
    - a (int | float): Primer número.
    - b (int | float): Segundo número.

    Retorna:
    - float: Resultado de la operación con dos decimales.

    Excepciones:
    - ValueError: Si los parámetros no son numéricos o la operación es inválida.
    - ZeroDivisionError: Si se intenta dividir o calcular el módulo por cero.
    """

    operaciones_validas = {
        "suma": lambda x, y: x + y,
        "resta": lambda x, y: x - y,
        "multiplicacion": lambda x, y: x * y,
        "division": lambda x, y: x / y,
        "potencia": lambda x, y: x ** y,
        "modulo": lambda x, y: x % y
    }

    # Validación de tipos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los parámetros deben ser numéricos (int o float)")

    # Validación de operación
    if operacion not in operaciones_validas:
        raise ValueError(
            f"Operación inválida: '{operacion}'. Operaciones válidas: suma, resta, multiplicacion, division, potencia, modulo"
        )

    # Validación de división por cero
    if operacion in ["division", "modulo"] and b == 0:
        raise ZeroDivisionError(f"No se puede realizar {operacion} por cero")

    # Ejecución de la operación
    resultado = operaciones_validas[operacion](a, b)
    return round(resultado, 2)

# Ejemplos de uso de todos los operadores
print(calculadora_cientifica("suma", 5, 3))             # 8.0
print(calculadora_cientifica("resta", 10, 4))           # 6.0
print(calculadora_cientifica("multiplicacion", 2, 3))   # 6.0
print(calculadora_cientifica("division", 10, 3))        # 3.33
print(calculadora_cientifica("potencia", 2, 8))         # 256.0
print(calculadora_cientifica("modulo", 10, 3))          # 1.0

# ejemplos de uso que generan errores
calculadora_cientifica("division", 10, 0)

calculadora_cientifica("raiz", 4, 2)

calculadora_cientifica("suma", "10", 2)

calculadora_cientifica("modulo", 5, None)
