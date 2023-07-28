# Bucles
# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for
inicio = 1
max = 10


def imprimir_numeros(max_number):
    for i in range(inicio, max_number):
        print(i)


imprimir_numeros(10)

# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while

numero = 0
while numero <= 20:
    if numero % 2 == 0:
        print(numero)
    numero += 1


# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100
x = 1
suma = 0
while x <= 100:
    suma = suma + x
    x += 1
print("suma total es, ", suma)
