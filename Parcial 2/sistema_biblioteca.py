# Excepciones personalizadas para el sistema de biblioteca

class ErrorBiblioteca(Exception):
    """Excepción base para el sistema de biblioteca."""
    pass


class LibroNoEncontrado(ErrorBiblioteca):
    """Se lanza cuando un libro no existe en el catálogo."""
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Libro con ISBN {isbn} no encontrado")


class LibroNoDisponible(ErrorBiblioteca):
    """Se lanza cuando no hay copias disponibles de un libro."""
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        super().__init__(f"No hay copias disponibles de '{titulo}'")


class UsuarioNoRegistrado(ErrorBiblioteca):
    """Se lanza cuando el usuario no está registrado en el sistema."""
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        super().__init__(f"Usuario con ID '{id_usuario}' no está registrado")


class LimitePrestamosExcedido(ErrorBiblioteca):
    """Se lanza cuando el usuario excede el límite de préstamos permitidos."""
    def __init__(self, id_usuario, limite):
        self.id_usuario = id_usuario
        self.limite = limite
        super().__init__(f"Usuario {id_usuario} excede límite de {limite} préstamos")


class PrestamoVencido(ErrorBiblioteca):
    """Se lanza cuando se intenta renovar un préstamo vencido."""
    def __init__(self, id_prestamo, dias_retraso):
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        super().__init__(f"Préstamo {id_prestamo} está vencido por {dias_retraso} días")

from datetime import datetime, timedelta


class SistemaBiblioteca:
    """
    Sistema completo de gestión de biblioteca digital.

    Estructuras de datos:
    - catalogo: {isbn: {'titulo', 'autor', 'anio', 'categoria', 'copias_total', 'copias_disponibles'}}
    - usuarios: {id_usuario: {'nombre', 'email', 'fecha_registro', 'prestamos_activos', 'historial', 'multas_pendientes'}}
    - prestamos: {id_prestamo: {'isbn', 'id_usuario', 'fecha_prestamo', 'fecha_vencimiento', 'fecha_devolucion', 'multa'}}
    """

    def __init__(self, dias_prestamo=14, multa_por_dia=1.0, limite_prestamos=3):
        """
        Inicializa el sistema.

        Args:
            dias_prestamo: Días permitidos para cada préstamo
            multa_por_dia: Multa diaria por retraso
            limite_prestamos: Máximo de préstamos simultáneos por usuario
        """
        self.catalogo = {}
        self.usuarios = {}
        self.prestamos = {}
        self.dias_prestamo = dias_prestamo
        self.multa_por_dia = multa_por_dia
        self.limite_prestamos = limite_prestamos
        self.contador_prestamos = 1  # Para generar IDs únicos de préstamo

    # ============ GESTIÓN DE CATÁLOGO ============

    def agregar_libro(self, isbn, titulo, autor, anio, categoria, copias):
        """
        Agrega un libro al catálogo.

        Validaciones:
        - ISBN debe ser string de 13 dígitos
        - Título y autor no vacíos
        - Año entre 1000 y año actual
        - Copias >= 1

        Raises:
            ValueError: Si validaciones fallan
            KeyError: Si ISBN ya existe
        """
        if not isinstance(isbn, str) or not isbn.isdigit() or len(isbn) != 13:
            raise ValueError("ISBN debe ser un string de 13 dígitos")

        if not titulo or not autor:
            raise ValueError("Título y autor no pueden estar vacíos")

        anio_actual = datetime.now().year
        if not (1000 <= anio <= anio_actual):
            raise ValueError(f"Año inválido: debe estar entre 1000 y {anio_actual}")

        if copias < 1:
            raise ValueError("Debe haber al menos una copia del libro")

        if isbn in self.catalogo:
            raise KeyError(f"El libro con ISBN {isbn} ya existe en el catálogo")

        self.catalogo[isbn] = {
            'titulo': titulo,
            'autor': autor,
            'anio': anio,
            'categoria': categoria,
            'copias_total': copias,
            'copias_disponibles': copias
        }

    def actualizar_copias(self, isbn, cantidad_cambio):
        """
        Actualiza número de copias (añade o remueve).

        Raises:
            LibroNoEncontrado: Si ISBN no existe
            ValueError: Si resultado sería negativo
        """
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        libro = self.catalogo[isbn]
        nuevas_copias = libro['copias_total'] + cantidad_cambio
        nuevas_disponibles = libro['copias_disponibles'] + cantidad_cambio

        if nuevas_copias < 0 or nuevas_disponibles < 0:
            raise ValueError("No se puede reducir copias por debajo de cero")

        libro['copias_total'] = nuevas_copias
        libro['copias_disponibles'] = nuevas_disponibles

    def buscar_libros(self, criterio='titulo', valor='', categoria=None):
        """
        Busca libros por diferentes criterios.

        Args:
            criterio: 'titulo', 'autor', 'anio'
            valor: Valor a buscar (búsqueda parcial case-insensitive)
            categoria: Filtro opcional por categoría

        Returns:
            Lista de diccionarios con info de libros que coinciden
        """
        valor = str(valor).lower()
        resultados = []

        for isbn, datos in self.catalogo.items():
            campo = str(datos.get(criterio, '')).lower()
            coincide = valor in campo if criterio != 'anio' else str(datos['anio']) == valor
            misma_categoria = categoria is None or datos['categoria'].lower() == categoria.lower()

            if coincide and misma_categoria:
                resultados.append({
                    'isbn': isbn,
                    'titulo': datos['titulo'],
                    'autor': datos['autor'],
                    'anio': datos['anio'],
                    'categoria': datos['categoria'],
                    'copias_disponibles': datos['copias_disponibles']
                })

        return resultados
    def exportar_catalogo(self, archivo='catalogo.txt'):
        """
        Exporta catálogo a archivo de texto.
        Formato: ISBN|Título|Autor|Año|Categoría|Copias

        Maneja excepciones de archivo apropiadamente.
        """
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for isbn, datos in self.catalogo.items():
                    linea = f"{isbn}|{datos['titulo']}|{datos['autor']}|{datos['anio']}|{datos['categoria']}|{datos['copias_total']}\n"
                    f.write(linea)
        except Exception as e:
            print(f"Error al exportar catálogo: {e}")
            
    #gestion de Usuarios

    def registrar_usuario(self, id_usuario, nombre, email):
        """
        Registra un nuevo usuario.

        Validaciones:
        - Email debe contener '@' y '.'
        - Nombre no vacío
        - ID único

        Raises:
            ValueError: Si validaciones fallan
        """
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Email inválido")
        if id_usuario in self.usuarios:
            raise ValueError(f"El usuario con ID '{id_usuario}' ya está registrado")

        self.usuarios[id_usuario] = {
            'nombre': nombre,
            'email': email,
            'fecha_registro': datetime.now(),
            'prestamos_activos': [],
            'historial': [],
            'multas_pendientes': 0.0
        }

    def obtener_estado_usuario(self, id_usuario):
        """
        Obtiene estado completo del usuario.

        Returns:
            dict con: nombre, prestamos_activos, puede_prestar, multas_pendientes

        Raises:
            UsuarioNoRegistrado: Si usuario no existe
        """
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)

        usuario = self.usuarios[id_usuario]
        puede_prestar = (
            len(usuario['prestamos_activos']) < self.limite_prestamos and
            usuario['multas_pendientes'] <= 50
        )

        return {
            'nombre': usuario['nombre'],
            'prestamos_activos': usuario['prestamos_activos'],
            'puede_prestar': puede_prestar,
            'multas_pendientes': round(usuario['multas_pendientes'], 2)
        }
    
    ##Gestion de prestamos

    def prestar_libro(self, isbn, id_usuario):
        """
        Realiza un préstamo.

        Returns:
            id_prestamo: ID único del préstamo

        Raises:
            UsuarioNoRegistrado, LibroNoEncontrado, LibroNoDisponible,
            LimitePrestamosExcedido, ValueError (multas pendientes)
        """
        if id_usuario not in self.usuarios:
            raise UsuarioNoRegistrado(id_usuario)
        if isbn not in self.catalogo:
            raise LibroNoEncontrado(isbn)

        libro = self.catalogo[isbn]
        usuario = self.usuarios[id_usuario]

        if libro['copias_disponibles'] < 1:
            raise LibroNoDisponible(isbn, libro['titulo'])

        if len(usuario['prestamos_activos']) >= self.limite_prestamos:
            raise LimitePrestamosExcedido(id_usuario, self.limite_prestamos)

        if usuario['multas_pendientes'] > 50:
            raise ValueError("Usuario tiene multas pendientes superiores a $50")

        id_prestamo = f"P{self.contador_prestamos:06d}"
        self.contador_prestamos += 1

        fecha_prestamo = datetime.now()
        fecha_vencimiento = fecha_prestamo + timedelta(days=self.dias_prestamo)

        self.prestamos[id_prestamo] = {
            'isbn': isbn,
            'id_usuario': id_usuario,
            'fecha_prestamo': fecha_prestamo,
            'fecha_vencimiento': fecha_vencimiento,
            'fecha_devolucion': None,
            'multa': 0.0
        }

        libro['copias_disponibles'] -= 1
        usuario['prestamos_activos'].append(id_prestamo)

        return id_prestamo

    def devolver_libro(self, id_prestamo):
        """
        Procesa devolución de libro.

        Returns:
            dict: {'dias_retraso': int, 'multa': float, 'mensaje': str}

        Raises:
            KeyError: Si préstamo no existe
            ValueError: Si ya fue devuelto
        """
        if id_prestamo not in self.prestamos:
            raise KeyError(f"Préstamo {id_prestamo} no existe")

        prestamo = self.prestamos[id_prestamo]
        if prestamo['fecha_devolucion'] is not None:
            raise ValueError("El préstamo ya fue devuelto")

        fecha_actual = datetime.now()
        dias_retraso = max((fecha_actual - prestamo['fecha_vencimiento']).days, 0)
        multa = dias_retraso * self.multa_por_dia

        prestamo['fecha_devolucion'] = fecha_actual
        prestamo['multa'] = multa

        usuario = self.usuarios[prestamo['id_usuario']]
        usuario['prestamos_activos'].remove(id_prestamo)
        usuario['historial'].append(id_prestamo)
        usuario['multas_pendientes'] += multa

        libro = self.catalogo[prestamo['isbn']]
        libro['copias_disponibles'] += 1

        return {
            'dias_retraso': dias_retraso,
            'multa': round(multa, 2),
            'mensaje': "Devolución procesada correctamente"
        }

    def renovar_prestamo(self, id_prestamo):
        """
        Renueva préstamo por otros N días (si no está vencido).

        Raises:
            PrestamoVencido: Si ya está vencido
            KeyError: Si préstamo no existe
        """
        if id_prestamo not in self.prestamos:
            raise KeyError(f"Préstamo {id_prestamo} no existe")

        prestamo = self.prestamos[id_prestamo]
        fecha_actual = datetime.now()

        if fecha_actual > prestamo['fecha_vencimiento']:
            dias_retraso = (fecha_actual - prestamo['fecha_vencimiento']).days
            raise PrestamoVencido(id_prestamo, dias_retraso)

        prestamo['fecha_vencimiento'] += timedelta(days=self.dias_prestamo)


# Estadisticas y reporte

    def libros_mas_prestados(self, n=10):
        conteo = {}
        for p in self.prestamos.values():
            isbn = p['isbn']
            conteo[isbn] = conteo.get(isbn, 0) + 1

        ordenados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
        resultado = []
        for isbn, cantidad in ordenados[:n]:
            titulo = self.catalogo[isbn]['titulo']
            resultado.append((isbn, titulo, cantidad))
        return resultado

    def usuarios_mas_activos(self, n=5):
        actividad = []
        for id_usuario, datos in self.usuarios.items():
            total = len(datos['historial'])
            actividad.append((id_usuario, datos['nombre'], total))
        return sorted(actividad, key=lambda x: x[2], reverse=True)[:n]

    def estadisticas_categoria(self, categoria):
        total_libros = total_copias = copias_prestadas = 0
        popularidad = {}

        for isbn, datos in self.catalogo.items():
            if datos['categoria'].lower() == categoria.lower():
                total_libros += 1
                total_copias += datos['copias_total']
                prestadas = datos['copias_total'] - datos['copias_disponibles']
                copias_prestadas += prestadas
                popularidad[isbn] = popularidad.get(isbn, 0)

        for p in self.prestamos.values():
            if p['isbn'] in popularidad:
                popularidad[p['isbn']] += 1

        libro_mas_popular = max(popularidad.items(), key=lambda x: x[1])[0] if popularidad else None
        titulo = self.catalogo[libro_mas_popular]['titulo'] if libro_mas_popular else None
        tasa = (copias_prestadas / total_copias * 100) if total_copias else 0

        return {
            'total_libros': total_libros,
            'total_copias': total_copias,
            'copias_prestadas': copias_prestadas,
            'tasa_prestamo': round(tasa, 2),
            'libro_mas_popular': titulo
        }

    def prestamos_vencidos(self):
        vencidos = []
        fecha_actual = datetime.now()
        for id_prestamo, datos in self.prestamos.items():
            if datos['fecha_devolucion'] is None and fecha_actual > datos['fecha_vencimiento']:
                dias = (fecha_actual - datos['fecha_vencimiento']).days
                multa = dias * self.multa_por_dia
                libro = self.catalogo[datos['isbn']]
                vencidos.append({
                    'id_prestamo': id_prestamo,
                    'isbn': datos['isbn'],
                    'titulo': libro['titulo'],
                    'id_usuario': datos['id_usuario'],
                    'dias_retraso': dias,
                    'multa_acumulada': round(multa, 2)
                        })
    def reporte_financiero(self, fecha_inicio=None, fecha_fin=None):
        """
        Genera reporte financiero de multas.

        Args:
            fecha_inicio, fecha_fin: Rango de fechas (datetime)
            Si son None, usa todo el historial

        Returns:
            dict: {
                'total_multas': float,
                'multas_pagadas': float,
                'multas_pendientes': float,
                'prestamos_con_multa': int,
                'promedio_multa': float
            }
        """
        total_multas = 0.0
        multas_pagadas = 0.0
        prestamos_con_multa = 0

        for prestamo in self.prestamos.values():
            fecha_dev = prestamo['fecha_devolucion']
            if fecha_dev is None:
                continue  # No se ha devuelto, no se considera pagada

            if fecha_inicio and fecha_dev < fecha_inicio:
                continue
            if fecha_fin and fecha_dev > fecha_fin:
                continue

            multa = prestamo['multa']
            if multa > 0:
                multas_pagadas += multa
                prestamos_con_multa += 1
            total_multas += multa

        multas_pendientes = sum(
            usuario['multas_pendientes'] for usuario in self.usuarios.values()
        )

        promedio_multa = (
            multas_pagadas / prestamos_con_multa if prestamos_con_multa else 0.0
        )

        return {
            'total_multas': round(total_multas + multas_pendientes, 2),
            'multas_pagadas': round(multas_pagadas, 2),
            'multas_pendientes': round(multas_pendientes, 2),
            'prestamos_con_multa': prestamos_con_multa,
            'promedio_multa': round(promedio_multa, 2)
        }
## Casos de prueba 

# Crear instancia del sistema
biblioteca = SistemaBiblioteca(dias_prestamo=7, multa_por_dia=2.0, limite_prestamos=3)

# 1. Agregar libros al catálogo
biblioteca.agregar_libro("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programación", 5)
biblioteca.agregar_libro("9780135404676", "Python Crash Course", "Eric Matthes", 2019, "Programación", 3)
biblioteca.agregar_libro("9781449355739", "Fluent Python", "Luciano Ramalho", 2015, "Programación", 2)

# 2. Registrar usuarios
biblioteca.registrar_usuario("U001", "Ana García", "ana@email.com")
biblioteca.registrar_usuario("U002", "Carlos López", "carlos@email.com")

# 3. Realizar préstamos
try:
    id_p1 = biblioteca.prestar_libro("9780134685991", "U001")
    id_p2 = biblioteca.prestar_libro("9780135404676", "U001")
    print(f"Préstamos realizados: {id_p1}, {id_p2}")
except Exception as e:
    print(f"Error en préstamo: {e}")

# 4. Buscar libros por autor
resultados = biblioteca.buscar_libros(criterio='autor', valor='python')
print(f"Libros encontrados por autor: {len(resultados)}")

# 5. Simular devolución con retraso
# Forzar vencimiento
biblioteca.prestamos[id_p1]['fecha_vencimiento'] = biblioteca.prestamos[id_p1]['fecha_prestamo'] - timedelta(days=1)
resultado_dev = biblioteca.devolver_libro(id_p1)
print(f"Devolución con multa: {resultado_dev}")

# 6. Estadísticas
print("Libros más prestados:", biblioteca.libros_mas_prestados(3))
print("Estadísticas de categoría:", biblioteca.estadisticas_categoria("Programación"))
print("Reporte financiero:", biblioteca.reporte_financiero())

# 7. Exportar catálogo
biblioteca.exportar_catalogo("catalogo_backup.txt")

# 8. Excepción: ISBN no existe
try:
    biblioteca.prestar_libro("9999999999999", "U001")
except LibroNoEncontrado as e:
    print(f"Capturado correctamente: {e}")

# 9. Excepción: Exceder límite de préstamos
try:
    biblioteca.prestar_libro("9781449355739", "U001")
    biblioteca.prestar_libro("9780134685991", "U001")  # Ya prestado antes
except LimitePrestamosExcedido as e:
    print(f"Límite controlado: {e}")

# 10. Estado de usuario
estado = biblioteca.obtener_estado_usuario("U001")
print("Estado de usuario U001:", estado)