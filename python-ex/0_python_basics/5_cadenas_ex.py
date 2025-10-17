"""EJERCICIOS DE CADENAS EN PYTHON"""

# 1. Ejercicio: Pide al usuario una frase y cuenta cuántas vocales tiene.
print("Cuenta número de vocales: ")

vocales = "aeiou"

frase_user = str(input("Introduce una frase: "))
num_vocales = sum(1 for palabra in frase_user if palabra in vocales)

print(f"La palabra {frase_user} tiene {num_vocales} vocales.")


# 2. Ejercicio: Pide una palabra y comprueba si es un palíndromo (igual al revés).
print("Palíndromo")

palabra_user = str(input("Introduce una palabra: "))

if palabra_user == palabra_user[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")


# 3. Ejercicio: Dada una frase, elimina los espacios de los extremos y conviértela en forma (title())