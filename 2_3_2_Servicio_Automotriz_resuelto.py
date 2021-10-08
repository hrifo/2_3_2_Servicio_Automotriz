rut=input('Ingrese rut: ')
nombre_completo=input('Ingrese nombre completo: ')
marca=input('Ingrese marca del automovil: ')
modelo=input('Ingrese modelo: ')

print('Los servicios posibles para contratar son ls siguientes: ')
print('---------------------------------------------------------')
print('|Servicio \t\t\t Tiempo de espera \t|')
print('---------------------------------------------------------')
print('|1.-Revisión de 1.000km \t\t 2 horas \t|')
print('|2.-Cambio de aceite \t\t\t 1 hora \t|')
print('|3.-Revisión de frenos: \t\t 0,5 horas \t|')
print('|4.-Revisión de correas \t\t 0,5 horas \t|')
print('|5.-Revisión de luces \t\t\t 0,2 horas \t|')
print('|6.-Revisión de direccion \t\t 0,5 horas \t|')
print('|7.-Lavado de tapiz (sin costo) \t 0,5 horas \t|')
print('---------------------------------------------------------')

opcion=0
arreglo=[]
while(opcion !=8):
    opcion=int(input('Elija su opcion y presione enter(8 para salir): '))
    arreglo.append(opcion)

tiempo=0.0
for op in arreglo:
    if op==1:
        tiempo+=2.0
    elif op==2:
        tiempo+=1.0
    elif op==3:
        tiempo+=0.5
    elif op==4:
        tiempo+=0.5
    elif op==5:
        tiempo+=0.2
    elif op==6:
        tiempo+=0.5
    elif op==7:
        tiempo+=0.5

print(f'El tiempo total es {tiempo} horas')