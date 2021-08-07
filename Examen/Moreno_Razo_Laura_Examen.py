import random
datos=[]
r=0
scovid=0
ncovid=0
for i in range (100):
    #Para facilitar las pruebas se generaron datos aleatorios con la libreria random
    edad= random.randint(5,90)
    print (edad)
    #edad= input("Ingresa la edad: ") instruccion si se quiere introducir datos reales
    indicador= round(random.random (),1)
    print(indicador)
    #indicador=float(input("Ingresa el indicador entre 0 y 1: ")) instruccion si se quiere introducir datos reales
    reg=str(edad)+ ','+ str(indicador)+ '\n'
    datos.append(reg)

    if indicador< 0.8:
        ncovid+=1
           
    else:
        r= r + int(edad) #Acumulador de edad de infectados
        scovid+=1
        

#Calculo de semáforo
if scovid==0:
    print ("Estamos en semáforo verde\n")
elif 1<=scovid<=30:
    print ("\nEstamos en semáforo amarillo\n")

elif 31<=scovid<=70:
    print ("Estamos en semáforo naranja\n")

elif 71<=scovid<=100:
    print ("Estamos en semáforo rojo\n")
else:
    print ("Error\n")

#Calculo de promedio de edad en infectados
r= r/scovid
print ("El promedio de edad de personas con COVID es: "+ str(round(r,1))+"\n" )

print ("\t\t\tGracias por usar el programa\n")
print (datos)#Imprimir lista


#Guardar datos en archivo excel
a=open("covid.csv","a")
a.writelines(datos)
a.close()

#Abrir el archivo con los datos en modo lectura
with open('covid.csv', 'r') as fichero:
    for linea in fichero:
        print(linea, end='')


''' Existe un fallo en estas instrucciones,ya que no muestran el archivo
a=open('covid.csv','r')
contenido=a.read()
a.close()
print(contenido)
'''
