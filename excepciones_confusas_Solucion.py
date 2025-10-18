#CASO 1: Manejo de excepciones demasiado general
#Código
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except:  # ¡Captura TODO, incluso KeyboardInterrupt!
        print("Ocurrió un error")
        return None
    
## Problemas detectados

## aptura todo tipo de excepciones, incluso interrupciones del sistema.

## Oculta errores graves o de programación.

## Dificulta la depuración y el mantenimiento del código.

##Preguntas y respuestas

##  1. ¿Cómo sabrías qué salió mal en producción?
##  No podrías saberlo, porque el bloque except: oculta el tipo y el mensaje del error.

##  2. ¿Qué pasa si hay un error de tipeo en resultado?
##  El programa lo atraparía sin mostrar qué ocurrió, ocultando un NameError.

##  3. ¿Cómo afecta esto a la depuración?
##  Hace la depuración casi imposible, ya que no sabes qué tipo de error ocurrió ni en qué parte del código.

## CASO 2: Capturar todas las excepciones sin distinguirlas
## Código
def procesar_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'r')
        datos = archivo.read()
        archivo.close()
        
        numeros = [int(x) for x in datos.split()]
        promedio = sum(numeros) / len(numeros)
        return promedio
    except Exception as e:  # ¡Demasiado amplio!
        print(f"Error: {e}")
        return None
    
## Preguntas y respuestas

## 1. ¿Qué tipos específicos de errores pueden ocurrir?
## FileNotFoundError, PermissionError, ValueError, ZeroDivisionError.

##  2. ¿Deberían manejarse todos de la misma manera?
## No. Cada tipo de error requiere una acción diferente o un mensaje distinto.

##  3. ¿Qué información se pierde al capturar todo?
##  El tipo de error y el contexto en el que ocurrió, esenciales para depurar.

## CASO 3: Excepciones silenciadas con pass
## Código
def guardar_configuracion(config):
    try:
        with open('config.txt', 'w') as archivo:
            archivo.write(str(config))
    except:
        pass  # ¡El usuario no sabe que falló!

##  Preguntas y respuestas

##  1. ¿Qué debería suceder cuando falla el guardado?
# El programa debería informar el error (mostrar mensaje o registrar en log).

## 2. ¿Cómo informarías al usuario?
## Mostrando un mensaje claro o lanzando una excepción específica.

## 3. ¿Es este error algo que deberías manejar?
## Sí, pero sin ocultarlo. Es crítico que el usuario sepa si los datos no se guardaron.

## CASO 4: Orden y uso de try, except, else, finally
## Código
def operacion_confusa(tiene_error):
    try:
        if tiene_error:
            raise ValueError("Error simulado")
        print("Operación exitosa")
    except ValueError:
        print("Manejando error")
    else:
        print("Esto se ejecuta...")  # ¿Cuándo?
    finally:
        print("Esto siempre se ejecuta...")  # ¿Cuándo?

##  Preguntas y respuestas

## 1. ¿En qué se diferencia else de finally?

##  else: se ejecuta solo si no ocurre ninguna excepción.

##  finally: se ejecuta siempre, ocurra o no error.

##  2. ¿Cuándo usarías cada uno?

##  else: para código que debe correr solo si todo salió bien.

##  finally: para cerrar recursos o ejecutar acciones finales (siempre).

## 3. ¿Qué pasa si hay un return en try?
## El bloque finally se ejecuta antes de que la función retorne, garantizando limpieza o registros.




##  CASO 5: Uso incorrecto de raise
##  Código


# A: Raise genérico
def validar_edad(edad):
    if edad < 0:
        raise Exception("Edad inválida")

# B: Mensaje no informativo
def dividir(a, b):
    if b == 0:
        raise ValueError("Error")

# C: Tipo de excepción incorrecto
def abrir_archivo(nombre):
    if not nombre:
        raise ValueError("Nombre vacío")
    
## Preguntas y respuestas

## 1. ¿Qué tipo de excepción sería más apropiado?

## A: ValueError("La edad no puede ser negativa")

## B: ZeroDivisionError("No se puede dividir entre cero")

## C: FileNotFoundError("El nombre del archivo está vacío o no existe")

## 2. ¿Qué información debería incluir el mensaje?

## Debe explicar qué ocurrió, qué valor causó el error y qué se esperaba.

#  3. ¿Cómo ayuda esto a quien llama la función?

## Permite manejar errores específicos, entender el contexto y tomar acciones adecuadas sin revisar el código fuente.


##  CASO 6: No Re-lanzar Apropiadamente
##  Código base


def operacion_interna():
    try:
        # Operación crítica
        resultado = procesar_datos_criticos()
        return resultado
    except Exception as e:
        print(f"Error interno: {e}")
        return None  # ¿Es correcto ocultar el error?
    
##  Preguntas para reflexionar

##  ¿Cuándo deberías capturar y manejar?
##  Cuando el error puede resolverse localmente (ej. reintentar conexión, pedir otro archivo, etc.).

##  ¿Cuándo deberías capturar, registrar y re-lanzar?
##  Cuando quieres registrar información para diagnóstico, pero dejar que otro nivel decida qué hacer.

##  ¿Cuándo no deberías capturar en absoluto?
##  Cuando no puedes manejarlo ni aportar información útil — deja que la excepción se propague.

##  CASO 7: Excepciones en Bucles
##  Código base
def procesar_lista_malo(elementos):
    resultados = []
    for elemento in elementos:
        resultado = procesar(elemento)  # ¿Y si esto falla?
        resultados.append(resultado)
    return resultados


##  Preguntas para reflexionar

##  ¿Debería un error detener todo el proceso?
### No siempre. Si los elementos son independientes, conviene procesar lo que se pueda y reportar los fallos.

##  ¿Cómo reportarías múltiples errores?
##   Guardando los errores en una lista o archivo de log para revisarlos después.

##  ¿Qué pasa si todos los elementos fallan?
##  Deberías devolver un mensaje o lanzar una excepción global indicando que no hubo resultados válidos.
