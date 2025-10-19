def es_bisiesto(anio):
    """
    Retorna True si el año es bisiesto.
    Reglas:
    - Divisible por 4: bisiesto
    - EXCEPTO si es divisible por 100: no bisiesto
    - EXCEPTO si es divisible por 400: bisiesto
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def dias_en_mes(mes, anio):
    """
    Retorna el número de días en el mes (1-12).
    Considera años bisiestos para febrero.
    Lanza ValueError si el mes es inválido.
    """
    if not 1 <= mes <= 12:
        raise ValueError("Mes inválido. Debe estar entre 1 y 12.")

    dias_por_mes = {
        1: 31,
        2: 29 if es_bisiesto(anio) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return dias_por_mes[mes]


def generar_calendario(mes, anio, dia_inicio=0):
    """
    Genera una representación string del calendario del mes.
    dia_inicio: 0=Lunes, 1=Martes, ..., 6=Domingo

    Retorna string con formato:
    Lu Ma Mi Ju Vi Sa Do
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    ...
    """
    encabezado = "Lu Ma Mi Ju Vi Sa Do"
    calendario = [encabezado]

    dia_inicio = dia_inicio % 7  # Validación silenciosa
    dias = dias_en_mes(mes, anio)

    # Primera línea con espacios vacíos
    semana = ["   "] * dia_inicio

    for dia in range(1, dias + 1):
        semana.append(f"{dia:2}")
        if len(semana) == 7:
            calendario.append(" ".join(semana))
            semana = []

    if semana:
        calendario.append(" ".join(semana))

    return "\n".join(calendario)

print(es_bisiesto(2024))       # True
print(es_bisiesto(2100))       # False
print(es_bisiesto(2000))       # True

print(dias_en_mes(2, 2024))    # 29
print(dias_en_mes(2, 2023))    # 28

print(generar_calendario(1, 2025, 0))