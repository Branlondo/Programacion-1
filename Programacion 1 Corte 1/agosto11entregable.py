from itertools import product

def maximize_modulo():
    # Leer K y M
    K, M = map(int, input().split())
    
    # Leer las listas
    lists = []
    for _ in range(K):
        data = list(map(int, input().split()))
        lists.append(data[1:])  
    
    # Generar todas las combinaciones posibles
    max_value = 0
    for combo in product(*lists):
        total = sum(x**2 for x in combo) % M
        max_value = max(max_value, total)
    
    print(max_value)

# Ejemplo de uso
# Entrada:
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Salida esperada: 206
if __name__ == "__main__":
    maximize_modulo()
