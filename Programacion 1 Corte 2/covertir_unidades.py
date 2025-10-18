# ===========================================================================
# EJERCICIO 1: CONVERSOR DE UNIDADES (versión completa con validaciones)
# ===========================================================================

def convertir_unidad(valor, unidad_origen, unidad_destino, tipo):
    """
    Convierte entre diferentes unidades: temperatura, distancia o peso.
    
    Args:
        valor (float): Valor numérico a convertir.
        unidad_origen (str): Unidad de origen.
        unidad_destino (str): Unidad de destino.
        tipo (str): "temperatura", "distancia" o "peso".
    
    Returns:
        float: Valor convertido con 2 decimales.
    
    Raises:
        ValueError: Si se especifica un tipo o unidad no válida, 
                    o si las validaciones de entrada fallan.
    """

    # ------------------------------------------------------------
    # Validaciones de tipo de dato
    # ------------------------------------------------------------
    if not isinstance(valor, (int, float)):
        raise ValueError("El valor debe ser numérico (int o float).")

    tipo = tipo.lower()
    unidad_origen = unidad_origen.lower()
    unidad_destino = unidad_destino.lower()

    # ------------------------------------------------------------
    # TEMPERATURA
    # ------------------------------------------------------------
    if tipo == "temperatura":
        unidades_validas = {"celsius", "fahrenheit", "kelvin"}
        if unidad_origen not in unidades_validas or unidad_destino not in unidades_validas:
            raise ValueError("Unidades de temperatura válidas: Celsius, Fahrenheit, Kelvin.")

        # Validación: Kelvin no puede ser negativo
        if unidad_origen == "kelvin" and valor < 0:
            raise ValueError("El valor en Kelvin no puede ser negativo.")

        if unidad_origen == unidad_destino:
            return round(valor, 2)

        # Conversiones
        if unidad_origen == "celsius":
            if unidad_destino == "fahrenheit":
                return round((valor * 9/5) + 32, 2)
            elif unidad_destino == "kelvin":
                return round(valor + 273.15, 2)

        elif unidad_origen == "fahrenheit":
            if unidad_destino == "celsius":
                return round((valor - 32) * 5/9, 2)
            elif unidad_destino == "kelvin":
                return round((valor - 32) * 5/9 + 273.15, 2)

        elif unidad_origen == "kelvin":
            if unidad_destino == "celsius":
                return round(valor - 273.15, 2)
            elif unidad_destino == "fahrenheit":
                return round((valor - 273.15) * 9/5 + 32, 2)

    # ------------------------------------------------------------
    # DISTANCIA
    # ------------------------------------------------------------
    elif tipo == "distancia":
        factores = {
            "metros": 1,
            "kilometros": 1000,
            "millas": 1609.34,
            "pies": 0.3048
        }

        if unidad_origen not in factores or unidad_destino not in factores:
            raise ValueError("Unidades de distancia válidas: metros, kilometros, millas, pies.")

        # Conversión: a metros → destino
        valor_metros = valor * factores[unidad_origen]
        resultado = valor_metros / factores[unidad_destino]
        return round(resultado, 2)

    # ------------------------------------------------------------
    # PESO
    # ------------------------------------------------------------
    elif tipo == "peso":
        factores = {
            "gramos": 1,
            "kilogramos": 1000,
            "libras": 453.592,
            "onzas": 28.3495
        }

        if unidad_origen not in factores or unidad_destino not in factores:
            raise ValueError("Unidades de peso válidas: gramos, kilogramos, libras, onzas.")

        # Conversión: a gramos → destino
        valor_gramos = valor * factores[unidad_origen]
        resultado = valor_gramos / factores[unidad_destino]
        return round(resultado, 2)

    # ------------------------------------------------------------
    # Tipo no válido
    # ------------------------------------------------------------
    else:
        raise ValueError("Tipo de conversión no válido. Usa 'temperatura', 'distancia' o 'peso'.")


# ===========================================================================
# PRUEBAS DE EJEMPLO
# ===========================================================================
if __name__ == "__main__":
    print("Temperatura: 100°C → Fahrenheit =", convertir_unidad(100, "celsius", "fahrenheit", "temperatura"))
    print("Temperatura: 0 K → Celsius =", convertir_unidad(0, "kelvin", "celsius", "temperatura"))
    print("Distancia: 5 kilómetros → millas =", convertir_unidad(5, "kilometros", "millas", "distancia"))
    print("Peso: 70 kilogramos → libras =", convertir_unidad(70, "kilogramos", "libras", "peso"))
    print("Distancia: 560 pies -> millas = ",convertir_unidad(560,"pies","millas","distancia"))
