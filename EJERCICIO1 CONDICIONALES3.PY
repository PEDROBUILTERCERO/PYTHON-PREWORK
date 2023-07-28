# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos
n1 = int(input("Introducir primer nº: "))
n2 = int(input("Introducir segundo nº: "))
n3 = int(input("Introducir tercer nº: "))
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3
print(f"el numero mayor es:{mayor}")
