"""EJERCICIOS DE CONDICIONALES EN PYTHON"""
# 1. Ejercicio: Pide una edad al usuario y muestra si puede votar (mayor o igual a 18).
# Solicitar la edad al usuario.
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si la edad es mayor o igual a 18.
if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")


# 2. Ejercicio: Pide una nota y clasifícala como : Sobresaliente (>=9), Notable (>=7), Aprobado (>=5), Suspenso (<5)
# Solicitar la nota al usuario.
nota = float(input("Por favor, ingresa tu nota (0-10): "))

# Clasificar la nota.
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else: 
    print("Suspenso")


# 3. Ejercicio: Pide dos números y di cuál es mayor, menor o si son iguales.
# Solicitar dos números al usuario.
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número:"))

# Comparar los números
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}.")
elif num1 == num2:
    print(f"Los números {num1} y {num2} son iguales.")
else:
    print(f"El número {num1} es menor que {num2}.")