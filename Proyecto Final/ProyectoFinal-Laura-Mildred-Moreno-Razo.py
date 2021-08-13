import os
import pandas as pd

op=0


#Crear DataFrame con encabezados
def Data():
    global df
    df=pd.read_csv(r'Shinymakeup.csv', engine='python')
    df.columns = ['Nombre', 'Tipo', 'Código', 'Cantidad', 'Precio']


#Buscar producto por nombre
def Nombre():
    Data()
    buscar = input ("Ingrese el nombre del producto a buscar: \n")
    df2 = (df.loc[df['Nombre'].str.contains(buscar, case=False)])
    if df2.empty:
        print("\n\t\t\t\tProducto no encontrado ):\n")
    else:
        print(df2)  


#Total de productos
def total ():
    Data()
    print(df.sort_values(by=['Cantidad'],ascending=True)) #Ordenar por cantidad de productos en orden ascendiente
    suma= df['Cantidad'].sum()
    print ('El total de productos es: '+str(suma))
    
                                                               
#Modificar producto existente
def modificar():
    Data()
    s=input("¿Necesitas buscar el producto para recordar su código? 1)Si\n2)No: ")
    if s=='1':
        Nombre()
    codigo= input ("Ingresa el código del producto a modificar: ")
    
    m= input("\nSeleccione qué desea modificar: \n1)nombre\n2)tipo\n3)codigo\n4)cantidad\n5)precio\n")
    if m == '1':
        nombre= input("Ingrese el nuevo nombre: ")
        df.loc[df.Código== int(codigo), 'Nombre']= nombre #Encontrar producto por su codigo y cambiar columna seleccionada
        df.to_csv('Shinymakeup.csv', index= False,mode='w') 

    elif m=='2':
        tipo = input("Ingrese el nuevo tipo: ")
        df.loc[df.Código== int(codigo), 'Tipo']= tipo
        df.to_csv('Shinymakeup.csv', index= False) 


    elif m=='3':
        codigo= input("Ingrese el nuevo codigo: ")
        df.loc[df.Código== int(codigo), 'Código']= int(codigo)
        df.to_csv('Shinymakeup.csv', index= False) 

    elif m=='4':
        cantidad= input("Ingrese la nueva cantidad: ")
        df.loc[df.Código== int(codigo), 'Cantidad']= int(cantidad)
        df.to_csv('Shinymakeup.csv', index= False) 

    elif m=='5':
        precio= input("Ingrese el nuevo precio: ")
        df.loc[df.Código== int(codigo), 'Precio']= precio
        df.to_csv('Shinymakeup.csv', index= False)
        
    else:
        print ("Opción no válida, intenta de nuevo\n")

    



#Eliminar un producto
def borrar():
    Data()
    buscar = input ("Ingrese el código del producto a eliminar: ")
    n = df[df['Código']== int(buscar)].index
    df.drop(n ,inplace=True)
    print (df)
    df.to_csv("Shinymakeup.csv", index= False,mode='w') 




#Buscar producto por tipo
def tipo():
    Data()
    buscar = input ("Ingrese el tipo de productos a visualizar: \n")
    df2 = (df.loc[df['Tipo'].str.contains(buscar, case=False)])
    if df2.empty:
        print("\n\t\t\t\tTipo de producto no encontrado ):\n")
    else:
        print(df2)    




#Agregar producto
def añadir():
    #os.system("cls")
    nombre= input("Ingresa el nombre del producto: ")
    a=0
    while (a!=1):
        print("Selecciona entre las categorías disponibles")
        print ("1) Ojos\n2) Rostro\n3) Labios\n4) Brochas y accesorios\n5) Cuidado de la piel")
        tipo= input()
        if tipo== "1":
            tipo= "Ojos"
            a=1
        elif tipo== "2":
            tipo= "Rostro"
            a=1
            
        elif tipo== '3':
            tipo= "Labios"
            a=1
            
        elif tipo== '4':
            tipo= "Brochas y accesorios"
            a=1
            
        elif tipo== '5':
            tipo= "Cuidado de la piel"
            a=1
            
        else:
            print ("Opción no válida")

    codigo= input("Ingresa el código del producto: ")
    cantidad=input("Ingresa el número disponible de piezas del producto: ")
    precio= input("Ingresa el precio del producto: ")

    datos=[]
    reg= nombre + ','+ tipo + ',' + codigo + ',' +cantidad + ',' +precio +'\n'
    datos.append(reg)

    #Guardar producto en base de datos
    a=open("Shinymakeup.csv","a")
    a.writelines(datos)
    a.close()
    
    





    

#Menú
a=open("Shinymakeup.csv","a")
a.close()
while (op!=7):
        if os.stat("Shinymakeup.csv").st_size == 0: #Comprobar si el archivo esta vacío
            print ("Agrega al menos un producto para guardar")
            while os.stat("Shinymakeup.csv").st_size == 0: 
                añadir()
            
        print ("\n\t\t\t\t\t\t•♥•♥•♥•♥ ☜ Bienvenido al inventario de Shiny makeup store ☞ ♥•♥•♥•♥•♥•\n")
        print ("1) Añadir producto \n2) Modificar producto existente\n3) Buscar producto por nombre\n4) Buscar productos por tipo\n5) Total de piezas\n6) Eliminar producto\n7) Salir\n")
        op= int(input("Selecciona una opción: "))

        if op==1:
            añadir()

        elif op==2:
            modificar()

        elif op==3:
            Nombre()
            
        elif op==4:
            tipo()

        elif op==5:
            total()

        elif op==6:
            borrar()

        elif op==7:
            input('\n\t\t\t\t¸.•♥•.¸¸.•♥• Gracias por usar mi programa, haz click para salir •♥•.¸¸.•♥•.¸')

        else:
            print('\n\t\t\tOpción no válida\n')


