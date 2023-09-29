# Conceptos básicos de Python

# Variables y nombres de variables
nombre = "Juan"  # Una variable llamada "nombre" que almacena una cadena de caracteres
edad = 25       # Una variable llamada "edad" que almacena un número entero
altura = 1.75   # Una variable llamada "altura" que almacena un número decimal

# Operadores en Python
suma = 5 + 3     # Operador de suma
resta = 7 - 2    # Operador de resta
multiplicacion = 4 * 6  # Operador de multiplicación
division = 10 / 2       # Operador de división
modulo = 11 % 3         # Operador de módulo (resto de la división)

# Tipos de datos
tipo_nombre = type(nombre)   # La función type() devuelve el tipo de dato de una variable
tipo_edad = type(edad)
tipo_altura = type(altura)


tipo_numerico = int()
tipo_booleano = False or True
tipo_decimal = float()
tipo_string = str()


# Uso de str() para convertir números en strings
# Es necesario convertir las variables numéricas en strings antes de concatenarlas con strings.
mensaje = "Hola, mi nombre es " + nombre + ", tengo " + str(edad) + " años y mido " + str(altura) + " metros."

# Imprimir resultados USANDO STR PARA convertir numeros a texto para usar la funcion print :)
print("Operadores:")
print("Suma: " + str(suma))
print("Resta: " + str(resta))
print("Multiplicación: " + str(multiplicacion))
print("División: " + str(division))
print("Módulo: " + str(modulo))

print("Tipos de datos:")
print("Tipo de nombre: " + str(tipo_nombre))
print("Tipo de edad: " + str(tipo_edad))
print("Tipo de altura: " + str(tipo_altura))

print("Mensaje concatenado:")
print(mensaje)
