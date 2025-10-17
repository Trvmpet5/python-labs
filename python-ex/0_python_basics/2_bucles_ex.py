"""EJERCICIOS DE BUCLES EN PYTHON"""
# 1. Ejercicio: Imprime los números del 1 al 10 utilizando un bucle 'for'.
print("Números del 1 al 10:")
for i in range (10):
    print(i + 1)

# 2. Ejercicio: Impre los pares del 2 al 20.
# Opción 1: Realizando el salto en el rango.
print("Números pares del 2 al 20 (Opción 1):")
for i in range(2, 21, 2):
    print(i)

print("Números pares del 2 al 20 (Opción 2):")  
for i in range(20):
    if i%2 == 0:
        print(i)

# 3. Ejercicio: Recorre una lista de frutas e imprímelas una por una.
frutas = ["manzana", "plátano", "cereza", "naranja"]
print("Lista de frutas:")

for i in frutas:
    print(i)

#  4. Ejercicio: Pide al usuario 5 números y calcula la suma total.
suma_total = 0
# Pedir 5 número al usuario
for i in range(5):
    suma_total+= int(input("Introduce un número para sumar: "))

# 5. Ejercicio: Recorre la palabra "programar" y cuenta cuántas veces aparece la letra 'r'.
palabra = "programar"
contador_r = 0

# Recorrer la palabra y contar las 'r'
for letra in palabra:
    if letra == 'r':
        contador_r += 1

print(f"La letra 'r' aparece {contador_r} veces en la palabra '{palabra}'.")

# 6. Ejercicio con dificultad media: Haz un progrmama que pida al usuario un número n y dibuje una pirámide con ceros:
num = int(input("Introduce un número para dibujar la pirámide: "))
for n in range(num):
    print('0'*(n+1))