## 🟢 NIVEL 1: Básico (Operadores Fundamentales)
""""""""
### Ejercicio 1.1: Predice los Resultados
###python
# Evalúa sin ejecutar:
print(True and False)
print(True or False)
print(not True)
print(not False)

##**Tu predicción**: False
##                   True 
##                   False
##                   True
##**Resultado real**: False
##                    True
##                    False
##                    True

# Explicacion:  Con el operador "and" basta con que uno sea Falso para que el resultado sea "False" y "or" con que uno sea verdadero para que el resultado sea "True"
#el operador not  niega los booleanos.

### Ejercicio 1.2: Operadores Combinados

a, b, c = True, False, True

print(a and b)  # ?
print(a or b)   # ?
print(b or c)   # ?
print(a and c)  # ?

##Tus predicciones**: False, True, True, True

### Ejercicio 1.3: Precedencia

a, b, c = True, False, True

print(a and b or c)      # ?
print(a or b and c)      # ?
print(not a or b)        # ?
print(not (a or b))      # ?

##**Tus predicciones**: True, True, False, False

### Ejercicio 1.4: Comparaciones y Lógica

x = 5
print(x > 3 and x < 10)  # ?
print(x < 3 or x > 10)   # ?
print(not x > 3)         # ?

##**Tus predicciones**: True, False, False   


### Ejercicio 1.5: Comparaciones Encadenadas

x = 5
print(3 < x < 10)        # ?
print(1 <= x <= 3)       # ?
print(10 > x > 3)        # ?

###**Tus predicciones**: True,False,True

## 🟡 NIVEL 2: Intermedio (Valores y Cortocircuito)

### Ejercicio 2.1: Valores Retornados

print("hola" and "mundo")  # ?
print("hola" and "")       # ?
print("" and "mundo")      # ?
print("hola" or "mundo")   # ?
print("" or "mundo")       # ?

###**Tus predicciones**: mundo,"","",hola,mundo

### Ejercicio 2.2: Truthy y Falsy

print(bool(0))          # ?
print(bool(""))         # ?
print(bool([]))         # ?
print(bool([0]))        # ?
print(bool(" "))        # ?
print(bool(None))       # ?

###**Tus predicciones**: False, False, False, True, True, False

### Ejercicio 2.3: Evaluación de Cortocircuito

##Evalúa qué se imprime:


def f1():
    print("f1 ejecutada")
    return True

def f2():
    print("f2 ejecutada")
    return False

# Caso 1
print("Caso 1:")
resultado = f1() and f2()
print(f"Resultado: {resultado}")

# Caso 2
print("\nCaso 2:")
resultado = f2() and f1()
print(f"Resultado: {resultado}")

# Caso 3
print("\nCaso 3:")
resultado = f1() or f2()
print(f"Resultado: {resultado}")


##**Tu predicción**: False, False, True

### Ejercicio 2.4: Operadores de Pertenencia

nums = [1, 2, 3, 4, 5]
print(3 in nums)        # ?
print(6 in nums)        # ?
print(6 not in nums)    # ?

word = "Python"
print("P" in word)      # ?
print("p" in word)      # ?
print("th" in word)     # ?

##**Tus predicciones**: True, False, True, True, False, True

### Ejercicio 2.5: Identidad vs Igualdad

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)  # ?
print(lista1 is lista2)  # ?
print(lista1 == lista3)  # ?
print(lista1 is lista3)  # ?

##**Tus predicciones**: True, False, True, True

## 🔴 NIVEL 3: Avanzado (Aplicaciones Prácticas)

### Ejercicio 3.1: Validación de Formulario
#Implementa la función `validar_datos` que verifica si:
#- El nombre tiene entre 2 y 30 caracteres
#- El email contiene '@'
#- La edad es mayor o igual a 18
#- La contraseña tiene al menos 8 caracteres


def validar_datos(nombre, email, edad, contrasena):
    errores = []

    # Validar nombre
    if not (2 <= len(nombre) <= 30):
        errores.append("El nombre debe tener entre 2 y 30 caracteres.")

    # Validar email
    if '@' not in email:
        errores.append("El email debe contener '@'.")

    # Validar edad
    if edad < 18:
        errores.append("La edad debe ser mayor o igual a 18.")

    # Validar contraseña
    if len(contrasena) < 8:
        errores.append("La contraseña debe tener al menos 8 caracteres.")

    # Resultado final
    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True, "mensaje": "Todos los datos son válidos."}


# Ejemplo de uso
resultado = validar_datos("Ana", "ana@gmail.com", 22, "segura123")
print(resultado)

resultado2 = validar_datos("A", "correo.com", 15, "123")
print(resultado2)

# Pruebas
print(validar_datos("Ana", "ana@email.com", 25, "secreto123"))  # Debe ser True
print(validar_datos("", "no-email", 15, "123"))  # Debe ser False

#Ejercicio 3.2: Sistema de Autorización
#Implementa un sistema que determine si un usuario puede acceder a un recurso basado en:
#- Debe estar autenticado
#- Debe ser administrador O tener el permiso específico
#- No debe estar en la lista negra

def puede_acceder(autenticado, es_admin, tiene_permiso, en_lista_negra):
    """
    Determina si un usuario puede acceder a un recurso según:
    - Debe estar autenticado
    - Debe ser administrador O tener el permiso específico
    - No debe estar en la lista negra
    """
    if not autenticado:
        return "Acceso denegado: el usuario no está autenticado."

    if en_lista_negra:
        return "Acceso denegado: el usuario está en la lista negra."

    if es_admin or tiene_permiso:
        return "Acceso permitido."
    else:
        return "Acceso denegado: no tiene permisos suficientes."


# Ejemplos de uso:

# 1️⃣ Usuario autenticado y administrador
print(puede_acceder(autenticado=True, es_admin=True, tiene_permiso=False, en_lista_negra=False))
# ✅ Acceso permitido

# 2️⃣ Usuario autenticado con permiso específico
print(puede_acceder(autenticado=True, es_admin=False, tiene_permiso=True, en_lista_negra=False))
# ✅ Acceso permitido

# 3️⃣ Usuario autenticado pero sin permisos
print(puede_acceder(autenticado=True, es_admin=False, tiene_permiso=False, en_lista_negra=False))
# ❌ Acceso denegado

# 4️⃣ Usuario en lista negra
print(puede_acceder(autenticado=True, es_admin=True, tiene_permiso=True, en_lista_negra=True))
# ❌ Acceso denegado

# 5️⃣ Usuario no autenticado
print(puede_acceder(autenticado=False, es_admin=True, tiene_permiso=True, en_lista_negra=False))
# ❌ Acceso denegado

### Ejercicio 3.3: Acceso Seguro a Diccionario
#Implementa una función `obtener_valor_seguro` que retorne:
#- El valor de la clave si existe
#- Un valor predeterminado si la clave no existe

def obtener_valor_seguro(diccionario, clave, valor_predeterminado="Valor no encontrado"):
    """
    Retorna:
    - El valor de la clave si existe
    - Un valor predeterminado si la clave no existe
    """
    return diccionario.get(clave, valor_predeterminado)


# Ejemplo de uso:
datos = {
    "nombre": "Ana",
    "edad": 25,
    "pais": "Colombia"
}

print(obtener_valor_seguro(datos, "nombre"))          #  Ana
print(obtener_valor_seguro(datos, "ocupacion"))       #  Valor no encontrado
print(obtener_valor_seguro(datos, "ocupacion", "Desconocido"))  #  Desconocido

#Ejercicio 3.4: Filtrar Lista
#Escribe una función para filtrar una lista de productos según criterios:
#- Precio dentro de un rango (min y max)
#- Opcionalmente filtrar por categoría
#- Solo productos disponibles

def filtrar_productos(productos, precio_min, precio_max, categoria=None):
    """
    Filtra una lista de productos según:
    - Precio dentro de un rango (min y max)
    - Opcionalmente por categoría
    - Solo productos disponibles
    """
    filtrados = []

    for p in productos:
        if (
            p["disponible"] and
            precio_min <= p["precio"] <= precio_max and
            (categoria is None or p["categoria"] == categoria)
        ):
            filtrados.append(p)

    return filtrados


# Ejemplo de uso:
productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "Tecnología", "disponible": True},
    {"nombre": "Celular", "precio": 800, "categoria": "Tecnología", "disponible": True},
    {"nombre": "Bicicleta", "precio": 400, "categoria": "Deportes", "disponible": False},
    {"nombre": "Camiseta", "precio": 25, "categoria": "Ropa", "disponible": True},
    {"nombre": "TV", "precio": 950, "categoria": "Tecnología", "disponible": True}
]

# Filtrar por precio entre 100 y 1000, categoría "Tecnología"
resultado = filtrar_productos(productos, 100, 1000, categoria="Tecnología")
print("Productos filtrados:", resultado)

# Filtrar solo por rango de precio (sin categoría)
resultado2 = filtrar_productos(productos, 20, 1000)
print("Productos filtrados (sin categoría):", resultado2)



### Ejercicio 3.5: Evaluación de Riesgo
##  Implementa un sistema de evaluación de riesgo crediticio:

from typing import Dict, Any, Tuple, List

def _clamp(x, lo=0.0, hi=100.0):
    return max(lo, min(hi, x))

def calcular_puntaje(datos: Dict[str, Any]) -> float:
    """
    Calcula un puntaje 0-100 basado en:
      - income (ingreso anual)
      - deudas (deuda mensual total)
      - credit_history_score (0-100, mayor es mejor)
      - employment_years (años en empleo actual)
      - loan_amount (monto solicitado)
      - existing_defaults (bool)
    Si faltan llaves, se usan valores conservadores por defecto.
    """
    # Extraer con defaults razonables
    ingreso_anual = float(datos.get("income", 0.0))            # p.e. 30000
    deuda_mensual = float(datos.get("debt_monthly", 0.0))      # p.e. 500
    credit_hist = float(datos.get("credit_history_score", 50))# 0-100
    employment_years = float(datos.get("employment_years", 0))
    loan_amount = float(datos.get("loan_amount", 0.0))
    existing_defaults = bool(datos.get("existing_defaults", False))

    # 1) Debt-to-income ratio (DTI) mensual simple: (deuda_mensual * 12) / ingreso_anual
    dti = (deuda_mensual * 12) / (ingreso_anual + 1e-9)  # evitar división por 0
    # Convertir DTI a score (0-100) donde DTI bajo => score alto
    score_dti = _clamp((1.0 - dti) * 100.0)

    # 2) Credit history: asumido ya 0-100
    score_credit = _clamp(credit_hist)

    # 3) Employment stability
    score_emp = _clamp(employment_years * 10.0)  # cada año = 10 puntos hasta 100

    # 4) Loan-to-income (LTI) simple: loan_amount / ingreso_anual
    lti = loan_amount / (ingreso_anual + 1e-9)
    score_lti = _clamp((1.0 - lti) * 100.0)

    # Pesos (ajustables)
    W = {
        "credit": 0.35,
        "dti": 0.25,
        "emp": 0.15,
        "defaults": 0.20,  # se usa como penalización si existe; si no, se coloca en 0
        "lti": 0.05
    }

    # Si hay default, prepararemos penalización en vez de puntaje positivo
    score_defaults_component = 0.0 if not existing_defaults else 0.0

    # Suma ponderada de componentes "positivos"
    raw_score = (
        score_credit * W["credit"] +
        score_dti * W["dti"] +
        score_emp * W["emp"] +
        score_lti * W["lti"] +
        score_defaults_component * W["defaults"]
    )

    # Aplicar penalización por defaults históricos
    if existing_defaults:
        # penaliza fuertemente: reduce el puntaje final (factor ajustable)
        raw_score *= 0.60  # por ejemplo: deja 60% del puntaje calculado
        # además resta un valor fijo para enfatizar riesgo
        raw_score = _clamp(raw_score - 10.0)

    # Redondear a 2 decimales
    return round(_clamp(raw_score), 2)


def evaluar_riesgo(datos: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evalúa el riesgo y devuelve:
      - score: float 0-100
      - categoria: 'Bajo' | 'Medio' | 'Alto'
      - detalles: lista de strings explicando por qué
      - recomendaciones: lista de strings
    """
    score = calcular_puntaje(datos)
    detalles: List[str] = []
    recomendaciones: List[str] = []

    # Reglas de clasificación (umbrales)
    if score >= 75:
        categoria = "Bajo"
    elif score >= 50:
        categoria = "Medio"
    else:
        categoria = "Alto"

    # Añadir detalles explicativos basados en los mismos factores
    ingreso_anual = float(datos.get("income", 0.0))
    deuda_mensual = float(datos.get("debt_monthly", 0.0))
    credit_hist = float(datos.get("credit_history_score", 50))
    employment_years = float(datos.get("employment_years", 0))
    loan_amount = float(datos.get("loan_amount", 0.0))
    existing_defaults = bool(datos.get("existing_defaults", False))

    dti = (deuda_mensual * 12) / (ingreso_anual + 1e-9)
    lti = loan_amount / (ingreso_anual + 1e-9)

    # Detalles
    detalles.append(f"Puntaje calculado: {score}/100 ({categoria})")
    detalles.append(f"Historial crediticio: {credit_hist}/100")
    detalles.append(f"DTI (deuda/ingreso anual): {dti:.2f} -> {'alto' if dti>0.4 else 'aceptable' if dti<=0.4 else 'desconocido'}")
    detalles.append(f"Años en empleo actual: {employment_years}")
    detalles.append(f"Loan-to-income (LTI): {lti:.2f}")
    if existing_defaults:
        detalles.append("Historial de morosidades/registros negativos detectado (penalización aplicada).")

    # Recomendaciones simples
    if categoria == "Bajo":
        recomendaciones.append("Aprobación probable. Mantener buen comportamiento de pago.")
        recomendaciones.append("Revisar que documentación esté actualizada y validar términos del crédito.")
    elif categoria == "Medio":
        recomendaciones.append("Evaluación adicional recomendada: solicitar aval o revisar garantías.")
        recomendaciones.append("Reducir DTI (pagar deudas) o aumentar evidencia de ingresos para mejorar puntaje.")
    else:  # Alto
        recomendaciones.append("Alta probabilidad de rechazo. Requiere mitigación (aval, cosignatario o mayor entrada).")
        recomendaciones.append("Corregir historial crediticio y reducir deudas antes de re-aplicar.")

    return {
        "score": score,
        "categoria": categoria,
        "detalles": detalles,
        "recomendaciones": recomendaciones
    }


# -------------------------
# Ejemplos de uso
# -------------------------

if __name__ == "__main__":
    ejemplo_bueno = {
        "income": 60000,            # ingreso anual
        "debt_monthly": 300,        # deuda mensual
        "credit_history_score": 85, # 0-100
        "employment_years": 5,
        "loan_amount": 10000,
        "existing_defaults": False
    }

    ejemplo_medio = {
        "income": 30000,
        "debt_monthly": 800,
        "credit_history_score": 55,
        "employment_years": 2,
        "loan_amount": 15000,
        "existing_defaults": False
    }

    ejemplo_malo = {
        "income": 20000,
        "debt_monthly": 1000,
        "credit_history_score": 30,
        "employment_years": 0.5,
        "loan_amount": 12000,
        "existing_defaults": True
    }

    for nombre, ejemplo in [("Buen solicitante", ejemplo_bueno),
                            ("Solicitante medio", ejemplo_medio),
                            ("Alto riesgo", ejemplo_malo)]:
        resultado = evaluar_riesgo(ejemplo)
        print("=== ", nombre, "===")
        print("Score:", resultado["score"])
        print("Categoría:", resultado["categoria"])
        print("Detalles:")
        for d in resultado["detalles"]:
            print("  -", d)
        print("Recomendaciones:")
        for r in resultado["recomendaciones"]:
            print("  -", r)
        print()
