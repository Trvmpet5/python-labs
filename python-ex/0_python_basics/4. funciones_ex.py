"""EJERCICIOS DE FUNCIONES EN PYTHON"""

# 1. Ejercicio: Crea una función que reciba un nombre y da "Hola, [nombre]".
def func_respuesta(nombre):
    print(f"Hola, {nombre}")

# Ejemplo
func_respuesta("Isaías")


# 2. Ejercicio: Haz una función que reciba 2 números y devuelva su suma.
def func_suma(num1,num2):
    return num1+num2

# Ejemplo
print(func_suma(5,7))


# 3. Ejercicio: Crea una función que reciba un número y devuelva True si es par.
def func_es_par(num):
    if num%2 == 0:
        return True
    
    return False

# Ejemplo
print(func_es_par(6))


# 4. Ejercicio: Haz una función que reciba una lista y devuelva la media.
def func_media(lista):
    return sum(lista)/len(lista)

# Ejemplo
print(func_media([5,10,15]))


# 5. Ejercicio: Crea una función que reciba una palabra y devuelva cuántas vocales tiene.
vocales = "aeiou"

def func_num_vocales(palabra):
    num_vocales = sum(1 for letra in palabra.lower() if letra in vocales)
    return num_vocales

# Ejemplo
print(func_num_vocales("Aurelio"))


# 6. Ejercicio avanzado: Crea una función llamada evaluar_estudiante que reciba:
# - El nombre del estudiante (cadena de texto).
# - Una lista de calificaciones (números).
# - Un parámetro opcional mostrar = True/False (por defecto True).
# La función debe devolver:
# - El nombre del estudiante.
# - La media de las calificaciones.
# - Si está aprobado o no (aprobado si la media es >= 5).
# Si mostrar = False, no imprima nada, solo devuelva los valores.

def func_evaluar_estudiante(nombre, calificaciones, mostrar=True):
    if mostrar:
        print(f"Estudiante: {nombre}")
        print(f"Media de calificaciones: {func_media(calificaciones)}")
        if func_media(calificaciones) >= 5:
            print("Estado: Aprobado")
        else:
            print("Estado: No Aprobado")

    return nombre, func_media(calificaciones), func_media(calificaciones) >= 5

# Ejemplo
func_evaluar_estudiante("María", [6, 7, 8, 5])
func_evaluar_estudiante("Juan", [4, 3, 5], mostrar=False)