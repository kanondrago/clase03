# Escriba un programa que permita al usuario ingresar “n”
# números enteros positivos y muestre el promedio aritmético.
# El ingreso de la información terminara cuando el usuario
# ingrese el valor “0”.

numero = int(input('ingrese un valor n: '))
promedio =0.0
conteo=0

print("Introduzca un numero (-1 para salir): ")
x=int(input())

while x!=-1:
    promedio = promedio + x
    conteo=conteo+1
    print("Introduzca el siguiente numero (-1 para salir): ")
    x=int(input())


promedio=promedio/conteo


print("el valor del promedio es: ",promedio)

