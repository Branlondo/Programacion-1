#!/usr/bin/env python3
"""
PARCIAL 2 - EJERCICIOS (Parte 1)
Estudiante: _______________________________
Fecha: ____________________________________
"""

# ===========================================================================
# EJERCICIO 1: EXPRESIONES ARITMÉTICAS (10 puntos)
# ===========================================================================

def calculadora_cientifica(operacion, a, b):
    """
    Realiza operaciones matemáticas con validación.
    
    Args:
        operacion: "suma", "resta", "multiplicacion", "division", "potencia", "modulo"
        a: Primer número (int o float)
        b: Segundo número (int o float)
    
    Returns:
        float: Resultado con 2 decimales de precisión
    
    Raises:
        ValueError: Si la operación es inválida o tipos incorrectos
        ZeroDivisionError: Si intenta dividir por cero
    """
    # TODO: Implementar validaciones y operaciones
    pass


# ===========================================================================
# EJERCICIO 2: EXPRESIONES LÓGICAS Y RELACIONALES (12 puntos)
# ===========================================================================

class ValidadorPassword:
    """Validador de contraseñas con reglas configurables."""
    
    def __init__(self, min_longitud=8, requiere_mayuscula=True, 
                 requiere_minuscula=True, requiere_numero=True, 
                 requiere_especial=True):
        """
        Inicializa el validador con reglas específicas.
        
        Args:
            min_longitud: Longitud mínima requerida
            requiere_mayuscula: Si debe tener al menos una mayúscula
            requiere_minuscula: Si debe tener al menos una minúscula
            requiere_numero: Si debe tener al menos un número
            requiere_especial: Si debe tener al menos un carácter especial
        """
        # TODO: Inicializar atributos
        pass
    
    def validar(self, password):
        """
        Valida password según las reglas configuradas.
        
        Args:
            password: Contraseña a validar
        
        Returns:
            tuple: (es_valido, lista_de_errores)
                   (True, []) si es válido
                   (False, ['error1', 'error2', ...]) si no es válido
        """
        # TODO: Implementar validaciones
        pass
    
    def es_fuerte(self, password):
        """
        Determina si el password es fuerte.
        Un password fuerte tiene al menos 12 caracteres,
        mayúsculas, minúsculas, números y caracteres especiales.
        
        Returns:
            bool: True si es fuerte, False en caso contrario
        """
        # TODO: Implementar
        pass


# ===========================================================================
# EJERCICIO 3: ESTRUCTURAS DE DATOS (15 puntos)
# ===========================================================================

class GestorInventario:
    """Sistema de gestión de inventario."""
    
    def __init__(self):
        """
        Inicializa el inventario.
        Estructura: {codigo: {'nombre', 'precio', 'cantidad', 'categoria'}}
        """
        # TODO: Inicializar estructuras de datos
        pass
    
    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """
        Agrega un producto al inventario.
        
        Raises:
            ValueError: Si el código ya existe
        """
        # TODO: Implementar
        pass
    
    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock de un producto.
        
        Args:
            cantidad_cambio: Positivo para añadir, negativo para reducir
        
        Raises:
            ValueError: Si producto no existe o stock resultante sería negativo
        """
        # TODO: Implementar
        pass
    
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Returns:
            list: Lista de tuplas (codigo, nombre, precio)
        """
        # TODO: Implementar
        pass
    
    def productos_bajo_stock(self, limite=10):
        """
        Encuentra productos con stock bajo el límite.
        
        Returns:
            dict: {codigo: cantidad} de productos bajo el límite
        """
        # TODO: Implementar
        pass
    
    def valor_total_inventario(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Suma de (precio * cantidad) de todos los productos
        """
        # TODO: Implementar
        pass
    
    def top_productos(self, n=5):
        """
        Retorna los N productos con mayor valor en inventario.
        
        Returns:
            list: Lista de tuplas (codigo, valor_total) ordenadas descendentemente
        """
        # TODO: Implementar
        pass


# ===========================================================================
# EJERCICIO 4: ESTRUCTURAS DE CONTROL (10 puntos)
# ===========================================================================

def es_bisiesto(anio):
    """
    Determina si un año es bisiesto.
    
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si divisible por 100: no bisiesto
    - EXCEPTO si divisible por 400: bisiesto
    
    Returns:
        bool: True si es bisiesto, False en caso contrario
    """
    # TODO: Implementar
    pass


def dias_en_mes(mes, anio):
    """
    Retorna el número de días en un mes específico.
    
    Args:
        mes: Número del mes (1-12)
        anio: Año (considera bisiestos)
    
    Returns:
        int: Número de días en el mes
    
    Raises:
        ValueError: Si mes es inválido (no está entre 1 y 12)
    """
    # TODO: Implementar
    pass


def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera representación string del calendario de un mes.
    
    Args:
        mes: Mes (1-12)
        anio: Año
        dia_inicio: Día de la semana del primer día (0=Lunes, 6=Domingo)
    
    Returns:
        str: Calendario formateado
        
    Formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    # TODO: Implementar
    pass


# ===========================================================================
# EJERCICIO 5: ESTRUCTURAS DE REPETICIÓN (13 puntos)
# ===========================================================================

def analizar_ventas(ventas):
    """
    Analiza lista de ventas y genera estadísticas.
    
    Args:
        ventas: Lista de dicts con 'producto', 'cantidad', 'precio', 'descuento'
    
    Returns:
        dict: {
            'total_ventas': float,
            'promedio_por_venta': float,
            'producto_mas_vendido': str,
            'venta_mayor': dict,
            'total_descuentos': float
        }
    """
    # TODO: Implementar
    pass


def encontrar_patrones(numeros):
    """
    Encuentra patrones en una secuencia de números.
    
    Returns:
        dict: {
            'secuencias_ascendentes': int,
            'secuencias_descendentes': int,
            'longitud_max_ascendente': int,
            'longitud_max_descendente': int,
            'numeros_repetidos': dict
        }
    """
    # TODO: Implementar
    pass


def simular_crecimiento(principal, tasa_anual, anios, aporte_anual=0):
    """
    Simula crecimiento de inversión con interés compuesto.
    
    Args:
        principal: Monto inicial
        tasa_anual: Tasa de interés (0.05 para 5%)
        anios: Número de años
        aporte_anual: Aporte adicional al inicio de cada año
    
    Returns:
        list: Lista de dicts con 'anio', 'balance', 'interes_ganado'
    """
    # TODO: Implementar
    pass


# ===========================================================================
# CASOS DE PRUEBA
# ===========================================================================

if __name__ == "__main__":
    print("="*70)
    print(" PRUEBAS DE EJERCICIOS")
    print("="*70)
    
    # Aquí puedes añadir tus propias pruebas
    
    print("\nEjercicio 1: Calculadora")
    # TODO: Pruebas
    
    print("\nEjercicio 2: Validador de Password")
    # TODO: Pruebas
    
    print("\nEjercicio 3: Gestor de Inventario")
    # TODO: Pruebas
    
    print("\nEjercicio 4: Calendario")
    # TODO: Pruebas
    
    print("\nEjercicio 5: Análisis de Datos")
    # TODO: Pruebas
