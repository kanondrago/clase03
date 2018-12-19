#Escriba un programa que pida dos números enteros
# y que escriba si el mayor es múltiplo del menor.


a = int(input('ingrese a : '))
b = int(input('ingrese b : '))


if a>b:
    mayor=a
    menor=b
else:
    mayor=b
    menor=a

resto=mayor%menor

if resto==0:
    print("\n\n",mayor," es multiplo de ", menor)
else:
    print("\n\n",mayor," no es multiplo de ", menor)
