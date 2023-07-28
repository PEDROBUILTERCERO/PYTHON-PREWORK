# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
def suma_pareja(grupo):
    suma = 0
    for unidad in grupo:
        suma += unidad
    return suma


grupo = [23, 12]
print(suma_pareja(grupo))


# 2. Ejercicio: Defineuna función que tome un número y retorne su factorial
def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i + 1
    return tmp


print(factorial(4))
print(factorial(5))


# 3. Ejercicio: Define una función que tome un número y determine si es primo.
def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False


print(es_primo(13))

# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma.


def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma


numeros = [1, 2, 3, 4, 5]
print(sumar_lista(numeros))


# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
def reverse(input):
    if len(input) <= 1:
        return input
    return reverse(input[1:]) + input[0]


if __name__ == "__main__":
    input = "Hola"
    rev = reverse(input)
    print(rev)
