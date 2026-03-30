#OPERADORES DE COMPARACIÓN
#Mayor que >
#Menor que <
#Mayor o igual que >=
#Menor o igual que <=
#Igual ==
#Diferente !=
#Siempre se recibe como resultado un booleano
# = asigna un valor a algo
# mi_variable= "hola mundo"
#mi_bool=10==25 El resultado va a ser False
#print(mi_bool)

#OPERADORES LÓGICOS
# and (Y) se han de cumplir ambas
# or (O) si se cumple aunque sea una solo vale
# not (NO) no se ha de cumplir ninguna de las 2
#mi_bool=4<5 and 5<6
#print(mi_bool)
#mi_bool=10==10 or 3==3
#print(mi_bool)
#texto= "Esta frase es breve"
#mi_bool=("frase" in texto) or("python" in texto)
#print(mi_bool)
#mi_bool= not "a"=="a"
#print(mi_bool)

#CONTROL DE FLUJO
#Permite al programa tomar decisiones
#x=True
#if x:
 #   print(True)
#else:
#    print(False)
#if 10>9:
#    print("Es correcto"

#mascota="perro"
#if mascota=="gato":
 #   print("Tienes un gato")
#elif mascota=="perro":
 #   print("Tienes un perro")
#else:
#    print("No se que animal tienes")

##edad= 16
#calificacion=9
#if edad<18:
  #  print("Eres menor de edad")
   # if calificacion>=7:
    #    print("Has sacado buena  nota")
    #else:
     #   print("No has sacado buena  nota")
#else:
 #   print("Eres adulto")

#LOOPS (BUCLES)
 #Cuando queremos que un bloque de código se ejecute mas de 1 vez
# FOR
#lista=["a","b","c"]

#for letra in lista:
 #   numero_letra=lista.index(letra)+1
  #  print(f"Letra: {numero_letra}: {letra}")

#lista1=["pablo","laura","fede","luis","julia"]

#for nombre in lista1:
 #   if nombre.startswith("l"):
  #      print(nombre)
  #  else:
   #     print("Nombre que no comienza con l")


#numeros=[1,2,3,4,5]
#mi_valor=0

#for numero in numeros:
#    mi_valor=mi_valor+numero

#print(mi_valor)

#palabra="python"

#for letra in palabra:
  #  print(letra)

#for a,b in [1,2],[3,4],[5,6]:
    #print(a)
   # print(b)

#dic={1:"a",2:"b",3:"c"}

#for key,value in dic.items():
 #   print(f"La clave es: {key} y el valr es {value}")

#BUCLE WHILE
#Se cumple mientras se cumpla una condición, sino no
#monedas= 5

#while monedas>0:
 #   print(f"Todavia tienes {monedas} monedas")
  #  monedas-=1
#else:
 #   print("No me queda dinero")

#respuesta="s"

#while respuesta=="s":
#respuesta=input("Ingrese su respuesta: (s/n)")
#else:
 #   print("Gracias")

#pass break y continue
#nombre=input("Ingrese su nombre: ")
#for letra in nombre:
 #   if letra=="r":
  #      break
   # print(letra)

#RANGO
#Solo acepta integers, el primer hueco es el empiece, el segundo hasta donde, y el tercero,
#de cuanto en cuanto va a saltar
#for numero in range(1,50,2):
 #   print(numero)

#ENUMERATE
lista=["a","b","c"]
#indice=0
#for item in lista:
 #   print(indice,item)
  #  indice=indice+1
#for indice,item in enumerate(lista):
 #   print(indice,item)

#mis_tuples=list(enumerate(lista))
#print(mis_tuples)

#ZIP
#Llega hasta el largo de la lista más corta, las combina
#nombres=["Ana","Hugo","Valeria"]
#edades=[65,29,42]
#ciudades=['lima','Madrid','Mexico']
#combinados=list(zip(nombres,edades,ciudades))
#for nombres,edades,ciudades in combinados:
 #   print(f"{nombres} tiene,{edades} años, y vive en {ciudades}")

#MIN Y MAX
#menor=min(58,96,72,64,35)
#mayor=max(58,96,72,64,35)
#lista=[58,97,37,42,12]
#print(max(lista))
#print(menor)
#print(mayor)

#nombres=["juan","pablo","alicia"]
#print(min(nombres))

#nombre="carlos"
#print(min(nombre))
#dic={1:45,2:11}
#print(min(dic.values()))

#RANDOM
#Elige un valor aleatorio entre 0-1
#from random import *
#aleatorio= random()
#print(aleatorio)
#Selecciona uno de las opciones que hay
#colores=["azul","rojo","verde"]
#aleatorio=choice(colores)
#print(aleatorio)
#Mezcla los valores insitu
#numeros=list(range(5,50,5))
#shuffle(numeros)
#print(numeros)

#COMPRENSIÓN DE LISTAS (manera dinámica de construir listas)
#palabra= "python"
#Con comprension
#lista=[letra for letra in palabra/ 'python']
#lista=[n if n *2 >10 else 'no' for n in range(0,21,2) ]
#pies=[10,20,30,40,50]
#metros=[n/ 3.281 for n in pies]
#Sin comprension de listas
#for letra in palabra:
 #   lista.append(letra)
#print(metros)

#MATCH ACTUALIZACION PYTHON 3.10
#Busca coincidencias
#serie="N-02"
#match serie:
 #   case "N-01":
  #      print('samsung')
   # case "N-02":
    #    print('nokia')
    #case "N-03":
     #   print('motorola')
    #case _:
     #   print('no existe ese producto')

#cliente={'nombre':"Federico",'edad':45,'ocupacion':'instructor'}
#pelicula={'titulo':'matrix','ficha_tecnica':{'protagonista':'keanu reeves','director':' lana y lillu wachowski'}}

#elementos=[cliente,pelicula,'libro']

#for e in elementos:
 #   match e:
  #      case {'nombre':nombre, 'edad':edad, 'ocupacion':ocupacion}:
   #         print('Es un cliente')
    #        print(nombre,edad,ocupacion)

     #   case {'titulo':titulo, 'ficha_tecnica':{'protagonista':protagonista,'director':director}}:
      #      print('Es una pelicula')
       #     print(titulo,protagonista,director)

        #case _:
         #   print('no se que es esto')