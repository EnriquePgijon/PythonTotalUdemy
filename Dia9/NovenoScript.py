#MODULO COLLECTIONS
#Counter sirve para contar elementos
#from collections import Counter
#from collections import defaultdict
#from collections import namedtuple
#numeros=[8,9,2,3,4,3,2,12,3,4,5,7,8,9]
#print(Counter("misisippi"))
#serie= Counter([1,2,3,45,6,7,8,5,3,2,1,22,1,1,1,1,2,2,3,3,45,6,])
#print(serie.most_common(2))
#print(list(serie))
#Defaultdic asigna un valor por defecto si no se encuentra
#mi_dic={"uno":"verde","dos":"azul","tres":"rojo"}
#print(mi_dic["dos"])
#mi_dic=defaultdict(lambda: "nada")
#mi_dic["uno"]="verde"
#print(mi_dic["dos"])
#print(mi_dic)
#Permite acceder a los datos de manera sencilla
#Persona= namedtuple("Persona",["nombre","altura","peso"])
#ariel=Persona("Ariel",1.76,79)
#print(ariel[2])

#MODULOS OS Y SHUTIL
import os
#Ruta en la cual te encuentras
#print(os.getcwd())
#archivo=open("curso.txt","w")
#archivo.write("texto de prueba")
#archivo.close()

#print(os.listdir())
import shutil
#Mover el archivo al escritorio
#shutil.move("curso.txt", "C:\\Users\\6003801\\Desktop")
#shutil.rmtree elimina todos los archivos de esa carpeta
#Lo manda a la papelera
#import send2trash
#send2trash.send2trash("C:\\Users\\6003801\\Desktop\\curso.txt")
#Recorre la carpeta superior y devuelve lo que tiene dentro
#print(os.walk())

#for carpeta, subcarpeta, archivo in os.walk(ruta):
 #   print(f"En la carpeta: {ruta})
    #print("Las subcarpetas son:")
#    for sub in subcarpeta:
 #       print(f"\t{sub}")
  #  print(f"Los archivos son: ")
   # for arch in archivo:
    #    if arch.startswith("2015"):
     #       print(f"\t{arch}")

    #print("\n")

#MODULO DATETIME

from datetime import datetime
#mi_hora= datetime.time(17,35,50,1500)
#print(mi_hora)
#mi_dia= datetime.datetime(2025,10,17)
#print(mi_dia.today())
#mi_fecha= datetime(2025,5,15,22,10,15,2500)
#mi_fecha= mi_fecha.replace(month=11)
#print(mi_fecha)
#from datetime import date
#nacimiento= date(1995,3,5)
#defuncion=date(2095,6,19)
#vida= defuncion-nacimiento
#print(vida)
#despierta= datetime(2022,10,5,7,30)
#duerme= datetime(2022,10,5,23,45)
#vigilia=duerme-despierta
#print(vigilia)

#MODULOS PARA MEDIR EL TIEMPO
#Evalua cuanto tarda un codigo
#import time
#def prueba_for(numero):
 #   lista=[]
  #  for num in range(1,numero+1):
   #     lista.append(num)
    #return lista

#def prueba_while(numero):
 #   lista=[]
  #  contador=1
   # while contador<=numero:
    #    lista.append(contador)
     #   contador+=1
    #return lista
#inicio= time.time()
#prueba_for(15)
#final=time.time()
#print(final-inicio)

#inicio= time.time()
#prueba_while(15)
#final=time.time()
#print(final-inicio)

import timeit
#declaracion= '''
#prueba_for(10)


#mi_setup=
#def prueba_for(numero):
 #   lista=[]
  #  for num in range(1,numero+1):
   #     lista.append(num)
    #return lista


#duracion=timeit.timeit(declaracion,mi_setup,number=10000)
#print(duracion)

#declaracion2=
#prueba_while(10)


#mi_setup2=
#def prueba_while(numero):
#    lista=[]
 #   contador=1
  #  while contador<=numero:
   #     lista.append(contador)
    #    contador+=1
    #return lista


#duracion2=timeit.timeit(declaracion,mi_setup,number=10000)
#print(duracion)

#MODULO MATH
import math
#techo
#resultado=math.ceil(89.665)
#math.log(), .tan(), .cos.... hay muchos métodos completos
#print(resultado)

#MODULO RE
#Expresiones regulares
#/d digito numérico, /w valor alfanumérico, /s espacio en blanco
# /D NO numerico, /W NO alfanumerico, /S No espacio en blanco

#Cuantificadores: + 1 o mas veces, {n} se repite n veces, {n,m} se repite de n a m veces
#{n, } desde n hacia arriba, * 0 o más veces, ? 1 o 0 veces
import re
#texto="Si necesitas ayuda llama al (658) -598-9977 las 24 horas al servicio de ayuda online"
#patron= "ayuda"

#busqueda=re.findall(patron,texto)
#for hallazgo in re.findall(patron,texto):
 #   print(hallazgo)

#texto="llama al 564-525-6588 ya mismo"

#patron=r"/d{3}-/d{3}-/d{4}"

#resultado=re.search(patron,texto)
#print(resultado)

#clave=input("clave: ")
#patron=r'\D{1}\w{7}'
#chequea= re.search(patron,clave)
#print(chequea)

#texto="No atendemos los lunes por la tarde"
#Pone tantos caracteres como puntos pongas, $verifica si no hay un digito al final, y este al principio^
#buscar=re.search(r'.demos',texto)
#print(buscar)


#COMPRIMIR Y DESCOMPRIMIR ARCHIVOS
import zipfile
#mi_zip=zipfile.ZipFile('archivo_comprimido.zip','w')
#archivo que se va a comprimir
#mi_zip.write('mi_texto_A.txt')
#mi_zip.close()
#Descomprime el archivo
#zip_abierto=zipfile.ZipFile('archivo_comprimido.zip','r')
#zip_abierto.extractall()

import shutil
#carpeta_origen='C:\\USERS\\WIN10\\DESKTOP\\CARPETA_SUPERIOR'
#archivo_destino='Todo_Comprimido'
#shutil.make_archive(archivo_destino,'zip', carpeta_origen)
#Descomprimir usando shutil
#shutil.unpack_archive('Todo_comprimido.zip','Extraccion Terminada')