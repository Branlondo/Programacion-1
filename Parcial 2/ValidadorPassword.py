class ValidadorPassword:
    """
    Clase para validar contraseñas según reglas configurables.
    """

    def __init__(self, min_longitud=8, requiere_mayuscula=True,
                requiere_minuscula=True, requiere_numero=True,
                requiere_especial=True):
        """
        Inicializa los parámetros de validación.

        Parámetros:
        - min_longitud (int): Longitud mínima requerida.
        - requiere_mayuscula (bool): Requiere al menos una letra mayúscula.
        - requiere_minuscula (bool): Requiere al menos una letra minúscula.
        - requiere_numero (bool): Requiere al menos un dígito.
        - requiere_especial (bool): Requiere al menos un carácter especial.
        """
        self.min_longitud = min_longitud
        self.requiere_mayuscula = requiere_mayuscula
        self.requiere_minuscula = requiere_minuscula
        self.requiere_numero = requiere_numero
        self.requiere_especial = requiere_especial
        self.caracteres_especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    def validar(self, password):
        """
        Valida la contraseña según las reglas configuradas.

        Retorna:
        - (bool, list): Tupla con el estado de validez y lista de errores.
        """
        errores = []

        if not isinstance(password, str):
            errores.append("La contraseña debe ser una cadena de texto")
            return (False, errores)

        # Validaciones individuales
        if len(password) < self.min_longitud:
            errores.append(f"Longitud mínima no cumplida (mínimo {self.min_longitud} caracteres)")

        if self.requiere_mayuscula and not any(c.isupper() for c in password):
            errores.append("Falta al menos una letra mayúscula")

        if self.requiere_minuscula and not any(c.islower() for c in password):
            errores.append("Falta al menos una letra minúscula")

        if self.requiere_numero and not any(c.isdigit() for c in password):
            errores.append("Falta al menos un número")

        if self.requiere_especial and not any(c in self.caracteres_especiales for c in password):
            errores.append("Falta al menos un carácter especial")

        return (len(errores) == 0, errores)

    def es_fuerte(self, password):
        """
        Retorna True si la contraseña tiene al menos 12 caracteres,
        contiene mayúsculas, minúsculas, números y caracteres especiales.
        """
        return (
            isinstance(password, str) and
            len(password) >= 12 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in self.caracteres_especiales for c in password)
        )
    
validador = ValidadorPassword(min_longitud=8)

print(validador.validar("Abc123!"))         
# (False, ['Longitud mínima no cumplida (mínimo 8 caracteres)'])

print(validador.validar("Abc123!@"))        
# (True, [])

print(validador.validar("abcdefgh"))        
# (False, ['Falta al menos una letra mayúscula', 'Falta al menos un número', 'Falta al menos un carácter especial'])

print(validador.es_fuerte("Abc123!@#$Xyz")) 
# True