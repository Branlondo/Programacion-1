# ================================================
# Sistema de Control de Acceso
# ================================================

usuarios = [
    {
        "id": 1,
        "nombre": "Admin",
        "roles": ["admin"],
        "permisos": ["leer", "escribir", "eliminar"],
        "plan": "premium",
        "activo": True,
        "edad": 35
    },
    {
        "id": 2,
        "nombre": "Usuario Regular",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "basico",
        "activo": True,
        "edad": 17
    },
    {
        "id": 3,
        "nombre": "Usuario Premium Adulto",
        "roles": ["usuario"],
        "permisos": ["leer", "escribir"],
        "plan": "premium",
        "activo": True,
        "edad": 25
    },
    {
        "id": 4,
        "nombre": "Usuario Inactivo",
        "roles": ["usuario"],
        "permisos": ["leer"],
        "plan": "premium",
        "activo": False,
        "edad": 30
    },
]

recursos = [
    {
        "id": 1,
        "nombre": "Panel Admin",
        "requiere_rol": ["admin"],
        "requiere_permiso": "eliminar",
        "solo_premium": False,
        "solo_adultos": False
    },
    {
        "id": 2,
        "nombre": "Contenido Premium",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": True,
        "solo_adultos": False
    },
    {
        "id": 3,
        "nombre": "Contenido para Adultos",
        "requiere_rol": ["usuario", "admin"],
        "requiere_permiso": "leer",
        "solo_premium": False,
        "solo_adultos": True
    },
]

# ================================================
# Función principal de verificación
# ================================================
def puede_acceder_recurso(usuario, recurso):
    """
    Determina si un usuario puede acceder a un recurso
    y devuelve una tupla (bool, justificación)
    """

    # 1. Verificar si el usuario está activo
    if not usuario["activo"]:
        return (False, "El usuario no está activo en el sistema.")

    # 2. Verificar rol requerido
    if not any(rol in usuario["roles"] for rol in recurso.get("requiere_rol", [])):
        return (False, f"No posee el rol requerido ({recurso['requiere_rol']}).")

    # 3. Verificar permiso requerido
    if recurso.get("requiere_permiso") not in usuario["permisos"]:
        return (False, f"No tiene el permiso necesario ({recurso['requiere_permiso']}).")

    # 4. Verificar si es solo para usuarios premium
    if recurso.get("solo_premium", False) and usuario["plan"] != "premium":
        return (False, "Este recurso es solo para usuarios con plan premium.")

    # 5. Verificar si es contenido solo para adultos
    if recurso.get("solo_adultos", False) and usuario["edad"] < 18:
        return (False, "El contenido está restringido a mayores de edad.")

    # Si pasa todas las condiciones:
    return (True, "Acceso permitido. Todas las condiciones se cumplen.")


# ================================================
# Pruebas automáticas
# ================================================
def probar_accesos():
    print("=== RESULTADOS DE ACCESO ===\n")
    for usuario in usuarios:
        for recurso in recursos:
            puede, razon = puede_acceder_recurso(usuario, recurso)
            estado = "✅ PERMITIDO" if puede else "❌ DENEGADO"
            print(f"Usuario: {usuario['nombre']:<20} | Recurso: {recurso['nombre']:<25} | {estado}")
            print(f"  ↳ Justificación: {razon}")
        print("-" * 90)

# Ejecutar pruebas
probar_accesos()
