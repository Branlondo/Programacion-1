from abc import ABC, abstractmethod
from datetime import datetime, timedelta
 
# ====== ABSTRACCIÓN ======
class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True
 
    # Getters y Setters (ENCAPSULAMIENTO)
    def get_titulo(self):
        return self.__titulo
 
    def get_autor(self):
        return self.__autor
 
    def get_disponible(self):
        return self.__disponible
 
    def set_disponible(self, estado: bool):
        self.__disponible = estado
 
    # Métodos abstractos (ABSTRACCIÓN)
    @abstractmethod
    def calcular_fecha_devolucion(self):
        pass
 
    @abstractmethod
    def obtener_tipo(self):
        pass
 
    @abstractmethod
    def obtener_detalles(self):
        pass
 
 
# ====== HERENCIA + POLIMORFISMO ======
class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo, autor)
        self.__isbn = isbn
 
    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=15)
 
    def obtener_tipo(self):
        return "Libro"
 
    def obtener_detalles(self):
        return f"{self.obtener_tipo()}: {self.get_titulo()} - Autor: {self.get_autor()}, ISBN: {self.__isbn}"
 
 
class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, numero):
        super().__init__(titulo, autor)
        self.__numero = numero
 
    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=7)
 
    def obtener_tipo(self):
        return "Revista"
 
    def obtener_detalles(self):
        return f"{self.obtener_tipo()}: {self.get_titulo()} - Autor: {self.get_autor()}, Número: {self.__numero}"
 
 
class MaterialAudiovisual(MaterialBiblioteca):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.__formato = formato
 
    def calcular_fecha_devolucion(self):
        return datetime.now() + timedelta(days=3)
 
    def obtener_tipo(self):
        return "Material Audiovisual"
 
    def obtener_detalles(self):
        return f"{self.obtener_tipo()}: {self.get_titulo()} - Autor: {self.get_autor()}, Formato: {self.__formato}"
 
 
# ====== USUARIO ======
class Usuario:
    def __init__(self, cc, nombre, correo):
        self.__cc = cc
        self.__nombre = nombre
        self.__correo = correo
        self.__prestamos = []
 
    def get_nombre(self):
        return self.__nombre
 
    def prestar_material(self, material: MaterialBiblioteca):
        if material.get_disponible():
            material.set_disponible(False)
            fecha_dev = material.calcular_fecha_devolucion()
            self.__prestamos.append((material, fecha_dev))
            print(f"{self.__nombre} ha prestado {material.get_titulo()}. Debe devolverlo antes de {fecha_dev.date()}.")
        else:
            print(f"{material.get_titulo()} no está disponible.")
 
    def devolver_material(self, material: MaterialBiblioteca):
        for prestamo in self.__prestamos:
            if prestamo[0] == material:
                material.set_disponible(True)
                self.__prestamos.remove(prestamo)
                print(f"{material.get_titulo()} ha sido devuelto por {self.__nombre}.")
                return
        print(f"{self.__nombre} no tenía prestado {material.get_titulo()}.")
 
 
# ====== BIBLIOTECARIO ======
class Bibliotecario:
    def __init__(self, nombre, id_bibliotecario):
        self.__nombre = nombre
        self.__id_bibliotecario = id_bibliotecario
 
    def añadir_material(self, biblioteca, material: MaterialBiblioteca):
        biblioteca.agregar_material(material)
        print(f"{material.get_titulo()} añadido al sistema por {self.__nombre}.")
 
    def eliminar_material(self, biblioteca, material: MaterialBiblioteca):
        biblioteca.eliminar_material(material)
        print(f"{material.get_titulo()} eliminado del sistema por {self.__nombre}.")
 
 
# ====== BIBLIOTECA ======
class Biblioteca:
    def __init__(self):
        self.__materiales = []
        self.__usuarios = []
 
    def agregar_material(self, material: MaterialBiblioteca):
        self.__materiales.append(material)
 
    def eliminar_material(self, material: MaterialBiblioteca):
        if material in self.__materiales:
            self.__materiales.remove(material)
 
    def inventario_materiales(self):
        for material in self.__materiales:
            print(material.obtener_detalles())
 
    def agregar_usuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)
 
    def usuarios_registrados(self):
        for usuario in self.__usuarios:
            print(usuario.get_nombre())
 
 
# ====== DEMOSTRACIÓN ======
mi_biblioteca = Biblioteca()
 
# Materiales
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "123456")
revista1 = Revista("National Geographic", "Varios", 202)
dvd1 = MaterialAudiovisual("Matrix", "Wachowski", "DVD")
 
# Usuarios
usuario1 = Usuario(101, "Brandon", "bran@gmail.com")
mi_biblioteca.agregar_usuario(usuario1)

# Bibliotecario
biblio = Bibliotecario("Carlos", 1)
biblio.añadir_material(mi_biblioteca, libro1)
biblio.añadir_material(mi_biblioteca, revista1)
biblio.añadir_material(mi_biblioteca, dvd1)

print("\n--- Inventario ---")
mi_biblioteca.inventario_materiales()

print("\n--- Préstamos ---")
usuario1.prestar_material(libro1)
usuario1.prestar_material(revista1)

print("\n--- Devolución ---")
usuario1.devolver_material(libro1)

print("\n--- Inventario Final ---")
mi_biblioteca.inventario_materiales()
