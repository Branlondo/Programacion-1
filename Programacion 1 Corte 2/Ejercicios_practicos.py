##Ejercicio 1.1: Predice el Resultado
##python
print(5 + 3 * 2)

##Tu predicción**: ___11____  
##Resultado real**: ___11____
##Explicación**: primero multiplicamos (3 * 2 = 6) y luego (5+6= 11) 

##Ejercicio 1.2: Paréntesis
##python
print((5 + 3) * 2)

##Tu predicción**: ___16____
"*************************"
### Ejercicio 1.3: División
#python
print(10 / 2)
print(10 // 2)
print(10 % 2)
"*************************"
##Tus predicciones: ___5.0____, ____5___, ___0____

##Ejercicio 1.4: Potencia
##python
print(2 ** 3)
print(2 ^ 3)
"*************************"
##**Tus predicciones**: ___8____, ___1____
"*************************"
### Ejercicio 1.5: Negación
##python
print(5 - -3)
print(-5 * -3)
"*************************"
##Tus predicciones**: ___8____, ___15____ç
"*************************"


## 🟡 NIVEL 2: Intermedio (Expresiones Complejas)

### Ejercicio 2.1: Múltiples Operadores
###python
print(2 + 3 * 4 - 5)
"*************************"
##**Tu predicción**: ___9____  
##**Paso a paso**: (3*4=12) luego (2+12=14) despues (14-5=9)
"*************************"

### Ejercicio 2.2: División y Multiplicación
###python
print(20 / 4 * 2)
print(20 / (4 * 2))
"*************************"
##**Tus predicciones**: ___10____, ___2,5____

### Ejercicio 2.3: Módulo en Expresión
##python
print(17 % 5 + 2 * 3)
"*************************"
##**Tu predicción**: __8_____
"*************************"

### Ejercicio 2.4: Potencias Anidadas
##python
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)
"*************************"
##**Tus predicciones**: ___512____, ___64____
"*************************"

### Ejercicio 2.5: Expresión Compleja
##python
print(10 + 5 * 2 - 8 / 4 + 3)
"*************************"
##**Tu predicción**: ___21.0____  
##**Paso a paso**:
## 1. (5*2= 10) y (8/4= 2.0)
## 2. (10+10-2.0+3)= 21.0 luego empezamos a sumar de izquierda a derecha
"*************************"

## 🔴 NIVEL 3: Avanzado (Problemas del Mundo Real)

### Ejercicio 3.1: Cálculo de Impuestos
##Calcula el total con impuesto del 15% sobre una compra de $100.

##python
price = 100
tax_rate = 0.15
print("*************************")
# Escribe la expresión correcta:
total = price + (price * tax_rate)
print(total)
print("*************************")
### Ejercicio 3.2: Conversión de Temperatura
##Convierte 25°C a Fahrenheit usando la fórmula: F = (C × 9/5) + 32

###python
celsius = 25

# Escribe la expresión:
fahrenheit = (celsius * (9/5)) + 32
print("*************************")
print(f" {celsius}°C a  fahrenheit es {fahrenheit}°F")
print("*************************")
### Ejercicio 3.3: Promedio de Calificaciones
##Calcula el promedio de 3 calificaciones: 85, 90, 78

###python
grade1 = 85
grade2 = 90
grade3 = 78

# Escribe la expresión correcta:
average = (grade1 + grade2 + grade3) / 3
print(f"El promedio de las 3 notas es {average}")

### Ejercicio 3.4: Dividir Cuenta
## amigos van a cenar. La cuenta es $127.50. Calcula cuánto paga cada uno.

#python
total_bill = 127.50
num_people = 4

per_person = total_bill /num_people

print(f"el total que paga cada persona es ${per_person}")


### Ejercicio 3.5: Tiempo Restante
##Tienes 125 minutos. ¿Cuántas horas y minutos son?

###python
total_minutes = 125

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutos son {hours} horas con {minutes} minutos.")

## 📊 Ejercicios de Debugging

### Debug 1: Encuentra el Error
###python
# Este código debería calcular el promedio
a = 10
b = 20
c = 30
average = a + b + c / 3
print(f"Promedio: {average}")


##**¿Qué está mal?** El codigo primero deberia sumar a+b+c pero la no estar en parentesis divide primero c
## por ende deberia ser (a + b + c)/3

### Debug 2: Encuentra el Error
###python
# Calcular 20% de descuento sobre $50
##price = 50
##discount = 20
##final = price - discount * price
##print(f"Precio final: ${final}")


##**¿Qué está mal?** el descuento deberia ser 0.2 en vez de 20 para que asi aplique el 20% de descuento

price = 50
discount = 0.2
final = price - discount * price
print(f"Precio final: ${final}")

## ✅ Autoevaluación

#Marca los ejercicios que completaste correctamente:

### Nivel 1 (Básico)
#- [O] Ejercicio 1.1
#- [O] Ejercicio 1.2
#- [O] Ejercicio 1.3
#- [O] Ejercicio 1.4
#- [O] Ejercicio 1.5

### Nivel 2 (Intermedio)
#- [O] Ejercicio 2.1
#- [O] Ejercicio 2.2
#- [O] Ejercicio 2.3
#- [O] Ejercicio 2.4
#- [O] Ejercicio 2.5

### Nivel 3 (Avanzado)
# [O] Ejercicio 3.1
#- [O] Ejercicio 3.2
#- [O] Ejercicio 3.3
#- [O] Ejercicio 3.4
#- [O] Ejercicio 3.5

### Proyecto Final
#- [O] Calculadora básica
#- [X] Calculadora avanzada