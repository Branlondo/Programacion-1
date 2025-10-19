def analizar_ventas(ventas):
    """
    Analiza lista de diccionarios de ventas.

    Retorna:
    {
        'total_ventas': float,
        'promedio_por_venta': float,
        'producto_mas_vendido': str,
        'venta_mayor': dict,
        'total_descuentos': float
    }
    """
    total_ventas = 0
    total_descuentos = 0
    cantidades_por_producto = {}
    venta_mayor_valor = 0
    venta_mayor = {}

    for venta in ventas:
        cantidad = venta['cantidad']
        precio = venta['precio']
        descuento = venta['descuento']
        producto = venta['producto']

        valor_venta = cantidad * precio * (1 - descuento)
        ahorro = cantidad * precio * descuento

        total_ventas += valor_venta
        total_descuentos += ahorro

        cantidades_por_producto[producto] = cantidades_por_producto.get(producto, 0) + cantidad

        if valor_venta > venta_mayor_valor:
            venta_mayor_valor = valor_venta
            venta_mayor = venta

    promedio = total_ventas / len(ventas) if ventas else 0
    producto_mas_vendido = max(cantidades_por_producto, key=cantidades_por_producto.get)

    return {
        'total_ventas': round(total_ventas, 2),
        'promedio_por_venta': round(promedio, 2),
        'producto_mas_vendido': producto_mas_vendido,
        'venta_mayor': venta_mayor,
        'total_descuentos': round(total_descuentos, 2)
    }

def encontrar_patrones(numeros):
    """
    Encuentra patrones en lista de números.

    Retorna:
    {
        'secuencias_ascendentes': int,
        'secuencias_descendentes': int,
        'longitud_max_ascendente': int,
        'longitud_max_descendente': int,
        'numeros_repetidos': dict
    }
    """
    sec_asc = sec_desc = 0
    max_asc = max_desc = 0
    repeticiones = {}
    actual_asc = actual_desc = 1

    for i in range(1, len(numeros)):
        if numeros[i] > numeros[i - 1]:
            actual_asc += 1
            actual_desc = 1
        elif numeros[i] < numeros[i - 1]:
            actual_desc += 1
            actual_asc = 1
        else:
            actual_asc = actual_desc = 1

        if actual_asc == 2:
            sec_asc += 1
        if actual_desc == 2:
            sec_desc += 1

        max_asc = max(max_asc, actual_asc)
        max_desc = max(max_desc, actual_desc)

        repeticiones[numeros[i]] = repeticiones.get(numeros[i], 0) + 1

    # Ajustar para incluir el primer número si está repetido
    repeticiones[numeros[0]] = repeticiones.get(numeros[0], 0) + 1

    # Filtrar solo los que se repiten más de una vez
    repetidos = {num: count for num, count in repeticiones.items() if count > 1}

    return {
        'secuencias_ascendentes': sec_asc,
        'secuencias_descendentes': sec_desc,
        'longitud_max_ascendente': max_asc,
        'longitud_max_descendente': max_desc,
        'numeros_repetidos': repetidos
    }

def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.

    Retorna lista de diccionarios por año:
    [
        {'anio': 1, 'balance': 1050.0, 'interes_ganado': 50.0},
        ...
    ]
    """
    resultados = []

    for anio in range(1, anios + 1):
        principal += aporte_anual
        interes = principal * tasa_anual
        principal += interes
        resultados.append({
            'anio': anio,
            'balance': round(principal, 2),
            'interes_ganado': round(interes, 2)
        })

    return resultados

## Casos de prueba

ventas = [
    {'producto': 'Laptop', 'cantidad': 2, 'precio': 1000, 'descuento': 0.1},
    {'producto': 'Mouse', 'cantidad': 10, 'precio': 20, 'descuento': 0.0},
    {'producto': 'Laptop', 'cantidad': 3, 'precio': 1000, 'descuento': 0.15}
]
print(analizar_ventas(ventas))

numeros = [1, 2, 3, 2, 1, 2, 3, 4, 5, 3, 3, 3]
print(encontrar_patrones(numeros))

print(simular_crecimiento(1000, 0.05, 5, 100))