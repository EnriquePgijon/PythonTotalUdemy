#ABRIR LEER Y CERRAR ARCHIVOS
#mi_archivo= open('prueba.txt.txt')

#una_linea=mi_archivo.readline()
#print(una_linea.upper())

#una_linea=mi_archivo.readline()
#print(una_linea)

#una_linea=mi_archivo.readline()
#print(una_linea)

#for l in mi_archivo:
#    print("Aqui dice: "+ l)

#todas=mi_archivo.readlines()
#print(todas)
#mi_archivo.close()

#CREAR Y ESCRIBIR ARCHIVOS
#El segundo parametro es donde va la condicion del archivo
#W crea el nuevo archivo si no existe y borra el contenido y pone lo nuevo
#a acumula lo que se escriba, añade
# r solo lectura
#archivo= open('prueba1.txt','w')
#archivo.write('soy el nuevo texto')
#archivo.write('mundo')

#archivo.writelines(['Hola','mundo','aqui','estoy'])
#lista=['Hola','mundo','aqui','estoy']
#for p in lista:
 #   archivo.writelines(p+'\n')
#archivo.close()

#DIRECTORIOS
import os

#ruta= os.getcwd()
#print(ruta)
#Crear carpetas
#ruta= os.makedirs('C:\\Users\\6003801\\Desktop\\CursoPython\\alternativo\\otra')
#archivo=open('primer.txt')
#print(archivo.read())
#Borrar carpetas
#os.rmdir('C:\\Users\\6003801\\Desktop\\CursoPython\\alternativo\\otra')
#otro_archivo =open('C:\\Users\\6003801\\Desktop\\CursoPython\\alternativo\\otro_archivo.txt')
#print(otro_archivo.read())
#Nombre de base
#ruta='C:\\Users\\6003801\\Desktop\\CursoPython\\alternativo\\otro_archivo.txt'
#elemento= os.path.basename(ruta)
#elemento1=os.path.dirname(ruta)
#elemento2=os.path.split(ruta)
#print(elemento2)
#otro_archivo= open('C:\\Users\\6003801\\Desktop\\CursoPython\\alternativo\\primer.txt.txt')
#print(otro_archivo.read())
from pathlib import Path, PureWindowsPath
#Abrir archivos desde cualquier os
#carpeta= Path('C:/Users/6003801/Desktop/CursoPython/alternativo')
#archivo= carpeta / 'primer.txt'
#mi_archivo= open(archivo)
#print(mi_archivo.read())

#PATHLIB
#carpeta= Path('C:/Users/6003801/Desktop/CursoPython/alternativo/primer.txt.txt')
#Convierte la ruta en la de windows
#rutaWind=PureWindowsPath(carpeta)
#print(carpeta.read_text())
#print(carpeta.name)
#print(carpeta.suffix)
#print(carpeta.stem)
#if not carpeta.exists():
 #   print("Este archivo no existe")
#else:
#    print("Genial, existe")
#print(rutaWind)

#PATH
#Construye una ruta relativa
#base=Path.home()
#guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_familia.txt"))
#guia2= guia.with_name("La_Pedrera.txt")
#print(base)
#print(guia.parent.parent.parent)
#print(guia2)
#Recorrer los archivos txt de una ruta de archivos
#guia3=Path(Path.home(),"Europa")
#for txt in Path(guia3).glob("**/*.txt"):
#    print(txt)


#LIMPIAR CONSOLA

#from os import system
#nombre= input("Dime tu nombre: ")
#edad= input("Dime tu edad: ")
#Borrar lo innecesario de la consola, hay que modificar config de pycharm
#system('cls')
#print(f"Tu nombre es: {nombre} y tienes {edad} años")

#ARCHIVOS Y FUNCIONES










