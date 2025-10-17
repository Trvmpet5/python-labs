"""EJERCICIOS DE OPERADORES EN PYTHON"""
# ¿Puedo sumar una cadena de texto y un número? Haz un ejemplo, haciendo los cambios necesarios, si es el caso.

# Declaración de variables.
texto = "El número es: "
numero = 5

# Solución Opción 1: Conversión explícita a texto.
resultado1 = texto + str(numero)
print("Opción 1 - Concatenación con conversión a cadena:", resultado1)

# Solución Opción 2: Uso de f-strings (formato de cadena).
texto_sumado = f"{texto}{numero}"
print("Opción 2 - Uso de f-strings:", texto_sumado)

# Solución Opción 3: Uso de formato con el método format().
texto_sumado = "{}{}".format(texto, numero)
print("Opción 3 - Uso de format():", texto_sumado)