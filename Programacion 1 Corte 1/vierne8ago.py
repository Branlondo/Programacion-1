#Brandon Camilo Londoño Garcia

def cadenas(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    jugador1 = 0
    jugador2 = 0
    combinaciones_j1 = []
    combinaciones_j2 = []

    for i in range(len(palabra)):
        for j in range(i + 1, len(palabra) + 1):
            subcadena = palabra[i:j]
            if palabra[i] in vocales:
                jugador1 += 1
                combinaciones_j1.append(subcadena)
            else:
                jugador2 += 1
                combinaciones_j2.append(subcadena)

    print(f"Jugador 1 (vocales): {jugador1} puntos")
    print(f"Combinaciones: {combinaciones_j1}")
    print(f"Jugador 2 (consonantes): {jugador2} puntos")
    print(f"Combinaciones: {combinaciones_j2}")

    if jugador1 > jugador2:
        print("Ganador: Jugador 1")
    elif jugador2 > jugador1:
        print("Ganador: Jugador 2")
    else:
        print("Empate")

cadenas("murcielago")