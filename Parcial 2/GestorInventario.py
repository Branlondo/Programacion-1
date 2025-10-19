class GestorInventario:
    """
    Clase para gestionar un inventario de productos usando estructuras de datos.
    """

    def __init__(self):
        """
        Inicializa el inventario como un diccionario:
        {
            'codigo_producto': {
                'nombre': str,
                'precio': float,
                'cantidad': int,
                'categoria': str
            }
        }
        """
        self.inventario = {}

    def agregar_producto(self, codigo, nombre, precio, cantidad, categoria):
        """
        Agrega un producto al inventario.

        Lanza ValueError si el código ya existe.
        """
        if codigo in self.inventario:
            raise ValueError(f"El producto con código '{codigo}' ya existe.")
        self.inventario[codigo] = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad,
            'categoria': categoria
        }

    def actualizar_stock(self, codigo, cantidad_cambio):
        """
        Actualiza el stock del producto.

        - Positivo: añade unidades
        - Negativo: reduce unidades

        Lanza ValueError si el producto no existe o si el stock resultante sería negativo.
        """
        if codigo not in self.inventario:
            raise ValueError(f"Producto con código '{codigo}' no encontrado.")

        nuevo_stock = self.inventario[codigo]['cantidad'] + cantidad_cambio
        if nuevo_stock < 0:
            raise ValueError(f"Stock insuficiente para el producto '{codigo}'.")
        self.inventario[codigo]['cantidad'] = nuevo_stock

    def buscar_por_categoria(self, categoria):
        """
        Retorna una lista de tuplas (codigo, nombre, precio) de productos en la categoría dada.
        """
        return [
            (codigo, datos['nombre'], datos['precio'])
            for codigo, datos in self.inventario.items()
            if datos['categoria'] == categoria
        ]

    def productos_bajo_stock(self, limite=10):
        """
        Retorna un diccionario {codigo: cantidad} de productos con cantidad menor al límite.
        """
        return {
            codigo: datos['cantidad']
            for codigo, datos in self.inventario.items()
            if datos['cantidad'] < limite
        }

    def valor_total_inventario(self):
        """
        Retorna el valor total del inventario (precio * cantidad de todos los productos).
        """
        return sum(
            datos['precio'] * datos['cantidad']
            for datos in self.inventario.values()
        )

    def top_productos(self, n=5):
        """
        Retorna una lista de tuplas (codigo, valor_total) de los N productos
        con mayor valor en inventario, ordenados descendentemente.
        """
        productos_valorados = [
            (codigo, datos['precio'] * datos['cantidad'])
            for codigo, datos in self.inventario.items()
        ]
        productos_valorados.sort(key=lambda x: x[1], reverse=True)
        return productos_valorados[:n]
    
inv = GestorInventario()
inv.agregar_producto("P001", "Laptop", 1200.00, 15, "Electrónica")
inv.agregar_producto("P002", "Mouse", 25.50, 5, "Accesorios")
inv.agregar_producto("P003", "Teclado", 85.00, 8, "Accesorios")

inv.actualizar_stock("P001", -3)  # Reduce stock

print(inv.productos_bajo_stock(10))
# {'P002': 5, 'P003': 8}

print(inv.buscar_por_categoria("Accesorios"))
# [('P002', 'Mouse', 25.5), ('P003', 'Teclado', 85.0)]

print(inv.valor_total_inventario())
# 1200*12 + 25.5*5 + 85*8 = 14400 + 127.5 + 680 = 15207.5

print(inv.top_productos(2))
# [('P001', 14400.0), ('P003', 680.0)]