#Escribir un algoritmo que lea tres números reales y me diga,
# si se trata de un triangulo (La suma de dos lados cualesquiera
# debe ser mayor que el tercer lado), y que tipo de triangulo es
# (Equilátero: todos los lados son iguales, Isósceles: al menos dos
# lados son iguales, Escaleno: no tiene dos lados iguales).

a = int(input('ingrese a : '))
b = int(input('ingrese b : '))
c = int(input('ingrese b : '))

if a<b+c and b<a+c and c<a+b:
    print('\nEs un triangulo real')
    if a==b and b==c:
        print('\nse trata de un triangulo Equilatero')
    elif a==b or b==c or a==c:
        print('\nse trata de un triangulo Isosceles')
    elif a!=b and a!=c and b!=c:
        print('\nse trata de un triangulo Escaleno')

else:
    print('\nNo exite un triangulo con esos lados')








