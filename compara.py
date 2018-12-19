#Escriba un programa llamado compara.py que permitirá
# al usuario ingresar dos datos numéricos (años) y calculara
# la diferencia de días transcurridos.

anio1 = int(input('ingrese el año 1 : '))
anio2 = int(input('ingrese el año 2 : '))

diferencia = abs(anio1-anio2)*365

if diferencia==0:
    print('no puede ingresar el mismo año')
else:
    print('los dias transcurridos son: ',diferencia)










