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
print('|3.-Revisión de frenos \t\t\t 0,5 horas \t|')
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

servicios=''
for op in arreglo:
    if op==1:
        servicios+='Revision 1000kms,'
    elif op==2:
        servicios+='Cambio de aceite,'
    elif op==3:
        servicios+='Revisión de frenos,'
    elif op==4:
        servicios+='Revisión de correas,'
    elif op==5:
        servicios+='Revisión de luces,'
    elif op==6:
        servicios+='Revisión de direccion,'
    elif op==7:
        servicios+='Lavado de tapiz,'

servicios = servicios[:-1]
estado=''
val=False
while(val==False):
    print('Seleccione el estado del trabajo:')
    print('1.-Trabajando')
    print('2.-Terminado')
    print('3.-Entregado')
    estado_int = int(input(''))
    if estado_int==1:
        estado='Trabajando'
        val=True
    elif estado_int==2:
        estado='Terminado'
        val=True
    elif estado_int==3:
        estado='Entregado'
        val=True
    else:
        print('Opción no valida, reintente')

print('---------------------------------------------------------')
print('|\t\t SERVICIO AUTOMOTRIZ \t\t|')
print('---------------------------------------------------------')
print(f'Cliente: {nombre_completo}')
print(f'Servicios: {servicios}')
print(f'Cantidad: {len(arreglo)-1}')
print(f'Timpo de espera: {tiempo}')
print(f'Estado: {estado}')