#ANALIZADOR DE TEXTO

#Método index (LOS INDICES SIEMPRE EMPIEZAN EN 0, si es en orden inverso empieza en -1, siendo el 0 el último número)
#rindex busca al reves en reversa
#mi_texto="Esta es una prueba"
#resultado= mi_texto[9]
#print(resultado)
#resultado=mi_texto.index("n")
#print(resultado)

#Extraer sub-Strings cachos de texto

#texto="ABCDEFGHIJKLM"
# [2:5] Extrae todos los caracteres desde el 2 hasta el 5 pero sin incluirlo
# [2:] desde el 2 hasta el final
# [:5] desde el 0 hasta el 5 sin incluirlo
#[2:10:2] todos desde el 2 al 10 de 2 en 2
#[::3] todo desde el 0 hasta el final de 3 en 3
#[::-1] toda la cadena al reves, empezando por atrás
#[8::3] desde el 8 hasta el final de 3 en 3
#fragmento=texto[2:5]
#print(fragmento)

#MÉTODOS DE STRING

#texto="Este es el texto de Enrique"
#upper() pone el texto en mayusculas
#resultado=texto.upper()
#lower()
#resultado=texto.lower()
#Divide la lista por espacios por defecto, pero puedes poner una condicion para separar
#resultado=texto.split()
#resultado=texto.join()
#a="Aprender"
#b="Python"
#c="genial"
#e="-".join([a,b,c])
#find() devuelve -1 cuando no existe lo buscado
#resultado=texto.find("s")
#replace() replaza el primer por el segundo parámetro
#resultado=texto.replace("Enrique","HOLA")
#print(resultado)

#PROPIEDADES DE STRING

#Inmutabilidad, da error modificarlo desde el indice
#nombre="Carina"
#nombre[0]="K"
#print(nombre)
#Son concatenables
#n1="Ka"
#n2="rina"
#print(n1*4)
#pueden tener varias líneas
#poema=("""Mil pequeños peces blancos
#como si hirviera
#el color del agua""")
#print("agua" in poema)
#print(len(poema))

#LISTAS

#Pueden tener distintos tipos de datos a la vez y reemplazar cualquiera de sus elementos
#mi_lista=["a","b","c"]
#print(type(mi_lista))
#print(len(mi_lista))
#lista1=[1,2,3]
#Añade ese número en la ultima posición
#lista1.append(4)
#Quita el ultimo número
#lista1.pop()
#lista2=[4,5,6]
#lista1[0]="uno"
#print(lista1+lista2)
#mi_lista=["G","O","B","M"]
#Ordena en orden alfabético
#mi_lista.sort()
#Reverse devuelve la misma lista, pero al revés
#mi_lista.reverse()


#DICCIONARIOS
# pares clave:valor no importa el orden, solo la relacion con la clave del valor
#diccionario={"Paco":22,"Pepe":19}
#resultado=diccionario["Pepe"]
#print(resultado)
#cliente={"nombre":"Juan","apellido":"Fuentes","peso":70,"talla":1.76}
#print(cliente["talla"])
#dic={"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
#print(dic["c3"]["s2"])
#dic={"clave1":["a","b","c"],"clave2":["d","e","f"]}
#print(dic["clave2"][1].upper())
#Como se hace para añadir elementos a nuestro diccionario de manera dinamica
#dic={"1":"a","2":"b"}
#dic["3"]="c"
#print(dic.values())
#print(dic.keys())
#Dentro de los diccionarios tenemos tuplas por eso sale entre () cada par valor
#print(dic.items())

#TUPLAS
#ocupan menos espacio en memoria, almacenar estructuras que no queremos que sean modificadas
#tupla=(1,2,3,4,(10,20))
#tupla=list(tupla)
#print(tupla[4][0])
#t=(1,2,3)
#Asignar valores de la tupla a las variables, tienen que tener el mismo número
#x,y,z=t
#print(x,y,z)
#print(tupla)
#t=("hola",1,2.4)
#2  metodos count e index,
#t=(1,2,3,5)
#print(t.count(2))
#print(t.index(3))

#SETS
# declarar de 2 maneras, no permite duplicados, no ordenados en índices,
# no puedes reasignar valores
#set([1,2,3,4]) si has puesto set asi, solo admite un elemento, asique debe ir en corchete
#1,2,3,4,5,6}
#mi_set=set([1,2,3,4,5])
#print(type(mi_set))
#print(mi_set)
#otro_set={1,2,3,4,5}
#print(type(otro_set))
#print(otro_set)
#set=set([1,2,3,"hola",(2,3)])
#print(type(set))
#print(set)
#print(3 in set)
#set1={1,2,3}
#set2={4,5,6}
#método para unir sets
#s3=set1.union(set2)
#print(s3)
#añadir elemrntos a un set existente lo añade al final, si hay duplicaos solo muestra 1
#set1.add(4)
#Remove
#set1.remove(4)
#pop elimina un número aleatorio en las tuplas, clear los vacía
#set1.pop()
#print(set1)

#BOOLEANOS
#Solo puede tener dos valores true o false
#comparaciones >,<,>=,<=,==,!=, cada vez que inicialices una variable con este valor el
#resultado va a ser un bool
#var1=True
#var2=False
#print(type(var1))
#print(var1)
#Si pnes los parentesis vacios es falso
#numero=bool(5!=3)
#print(numero)
#lista=[1,2,3,4]
#control=5 in lista
#print(control)


