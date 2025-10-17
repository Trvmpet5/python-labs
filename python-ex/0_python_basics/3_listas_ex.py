"""EJERCICIOS DE LISTAS EN PYTHON"""
#  1. Ejercicio: Crea una lista con los nombres de 5 amigos y recórrela con un for.
amigos = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]

# Recorrer la lista e imprimir cada nombre.
for i in amigos:
    print(i)


# 2. Ejercicio: Pide 5 números al usuario, guárdalos en una lista y muestra su media 3.
numeros = []

# Pedir 5 números al usuario.
for i in range(5):
    numero = (int(input("Introduce un número: ")))
    numeros.append(numero)

# Calcular la media.
media = sum(numeros) / len(numeros)
print(f"La media de los números introducidos es: {media}")


# 3. Ejercicio: Crea una lista de números del 1 al 10 y elimina los pares.
numeros = list(range(1, 11))

# Eliminar los números pares.
numeros_sin_pares = [num for num in numeros if num % 2 != 0]
print("Lista sin números pares:", numeros_sin_pares)

# 4. Ejercicio: Dada una lista de palabras, muestra cuántas tienen más de 5 letras.
palabras = ["manzana", "sol", "elefante", "casa", "programación", "gato"]

# Cuántas tienen más de 5 letras
for palabra in palabras:
    if len(palabra)>5:
        print(palabra)

# 5. Crea una lista de temperaturas, y calcula la máxima, mínima y promedio.
temperaturas = [23.5, 18.2, 30.0, 15.6, 27.8, 22.1, 19.4]

# Cálculo de la máxima, mínima y promedio.
temp_max = max(temperaturas)
temp_min = min(temperaturas)
temp_prom = sum(temperaturas)/len(temperaturas)

print(f"Temperatura máxima: {temp_max}. Temperatura mínima: {temp_min}. Temperatura promedio: {temp_prom}")

# 6. Ejercicio avanzado: Haz un programa que lea números introducidos por el usuario hasta que escriba "fin" y luego muestre:
# Cuántos números se han introducido, la suma total y la media.
# El número más alto y el más bajo.

# Introducción de números por el usuario
palabra_user = 0
numeros_user = []

# Bucle recolección de números.
while True:
    palabra_user = input("Introduce un número: ")
    # Sentencia para escapar del bucle:
    if palabra_user == "fin":
        break
    
    try:
        numero = int(palabra_user)
        numeros_user.append(numero)
    except ValueError:
        print("Entrada no válida. Escribe un número o 'fin'.")

# Obtención de resultados.
cant_numeros = len(numeros_user)
suma_numeros = sum(numeros_user)
media_numeros = suma_numeros/cant_numeros
max_num = max(numeros_user)
min_num = min(numeros_user)

print(f"Cantidad de números introducidos: {cant_numeros}")
print(f"Suma total de los números: {suma_numeros}")
print(f"Media de los números: {media_numeros}")
print(f"Número más alto: {max_num}")    
print(f"Número más bajo: {min_num}")