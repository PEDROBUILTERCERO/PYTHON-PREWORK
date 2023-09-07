# Ejercicios nivel básico

# A Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.


def es_par(numero):
    return numero % 2 == 0


num = int(input("Ingresa un número: "))
if es_par(num):
    print("Es un número par.")
else:
    print("Es un número impar.")


# B.Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado


def calcular_factorial(numero):
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    elif numero == 0:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)


numero = 5
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")


# C. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
def contar_digitos(numero):
    return len(str(numero))


num = int(input("Ingresa un número: "))
print("La cantidad de dígitos es:", contar_digitos(num))


# D. Dada una lista de números, crea una función que devuelva el número máximo de la lista.
def encontrar_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo


numeros = [5, 12, 3, 8, 9]
print("El número máximo es:", encontrar_maximo(numeros))

# E 1. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.


def sumar_digitos(numero):
    cifras = [int(digito) for digito in str(numero)]
    suma = 0
    for cifra in cifras:
        suma = suma + cifra
    return suma


num = int(input("Ingresa un número: "))
suma_cifras = sumar_digitos(num)
print(f"la suma de las cifras de {num} es {suma_cifras}")

# F. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.


def calcular_mcd(x, y):
    while y:
        x, y = y, x % y
    return x


def mcm(x, y):
    if x == 0 or y == 0:
        return 0
    return int(abs(x * y) / calcular_mcd(x, y))


x = int(input("Ingrese el primer número "))
y = int(input("Ingrese el segundo número "))
print("El mcm es: ", mcm(x, y))


# G. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


base = float(input("ingrese primer nº "))
altura = float(input("ingrese segundo nº "))
area_del_triangulo = calcular_area_triangulo(base, altura)
print(f"El area es: {area_del_triangulo}")


# H. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
def numero_positivo_negativo(num):
    if num < 0:
        return "negativo"
    elif num > 0:
        return "positivo"
    else:
        return "cero"


num = float(input("ingresar un numero: "))
resultado = numero_positivo_negativo(num)
print(f"el numero ingresado es: {resultado}")

# ICrea una función que, dada una palabra, cuente la cantidad de letras en una palabra.


def contar_letras(palabra):
    cantidad_letras = len(palabra)
    return cantidad_letras


palabra = input("Ingresa una palabra: ")
resultado = contar_letras(palabra)
print(f"La palabra '{palabra}' tiene {resultado} letras.")


# J  Crea una función que, dada una lista de números, convierta la lista de númerosa su valor absoluto.
def valor_absoluto(lista):
    for i in range(len(lista)):
        lista[i] = abs(lista[i])
    return lista


lista = [5, -12, 3, -8, 9]
resultado = valor_absoluto(lista)
print(f"El valor absoluto de la lista es: {resultado}")


# K. Crea una función que, dado un número, verifique si un número es primo.
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True


numero = int(input("Ingresa un número: "))

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

# L #Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.


def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


num_1 = int(input("Ingresa el primer número: "))
num_2 = int(input("Ingresa el segundo número: "))
resultado = mcd(num_1, num_2)
print(f"El mcd es:  {resultado}")
