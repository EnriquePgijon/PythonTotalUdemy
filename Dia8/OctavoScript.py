#Instalar paquetes, crear modulos y paquetes, manejo de errores, detectar errores con pylint, probar codigo con unittest
#decoradores y generadores
#Pypi, pip install
#Cada archivo .py que tenemos es un modulo y podemos importar de uno a otro sus funciones etc
#Cada paquete debe tener __init__.py

#MODULOS Y PAQUETES
#def suma(num1, num2):
 #   print( num1 + num2)

#def resta(num1, num2):
 #   print( num1 - num2)


#MANEJO DE ERRORES
#Preparar nuestro código a los errores más comúnes
# try, except, finaly
#def suma1():
 #   n1= int(input("Numero 1: "))
  #  n2= int(input("Numero 2: "))
   # print(n1 + n2)
    #print("gracias por sumar"+n1)


#try:
    #Código que queremos probar
 #   suma1()
#except TypeError:
    #Codigo a ejecutar si hay un error
 #   print("Estas intentando concatenar tipos distintos")
#except ValueError:
 #   print("Eso no es un numero")
#else:
    #Codigo a ejecutar si no hay un error
 #   print("Hiciste todo bien")
#finally:
    #Código que se va a ejecutar igualmente
 #   print("Fin del programa")

#def pedir_numero():
#    while True:
        #try:
       #     numero = int(input("Introduce un numero: "))
      #  except:
     #       print("Eso no es un numero")
    #    else:
   #         print(f"Ingresaste el numero {numero}")
  #          break

 #   print("Gracias")
#pedir_numero()

#BUSCAR ERRORES CON PYLINT
#Poner esto en simbolo del sistema en tu archivo, pylint OctavoScript.py -r y
#numero1=500
#print(Numero1)

#PROBAR EL CÓDIGO CON UNITTEST
#biblioteca integrada


#DECORADORES
#funciones que modifican el comportamiento de otras funciones

#def cambiar_letras(tipo):
 #   def mayuscula(texto):
  #     print(texto.upper())

   # def minuscula(texto):
    #    print(texto.lower())

    #if tipo=="may":
     #   return mayuscula
    #elif tipo=="min":
     #   return minuscula

#def una_funcion(funcion):
 #   return funcion

#operacion= cambiar_letras("may")
#operacion("palabra")

#def decorar_saludo(funcion):
 #   def otra_funcion(palabra):
  #      print("Hola")
   #     funcion(palabra)
  #      print("Adios")
 #   return otra_funcion


#def mayusculas(texto):
 #      print(texto.upper())
#def minusculas(texto):
 #       print(texto.lower())

#mayuscula_decorada= decorar_saludo(mayusculas)
#mayuscula_decorada("palabra")

#GENERADORES
#Cuidan el espacio en memoria del ordenador, va produciendo a medida que se necesita
# yield para funciones generadoras en vez de return
def mi_funcion():
    lista=[]
    for i in range(1,5):
        lista.append(i*10)
    return lista

def mi_generador():
     for i in range(1,5):
         yield i*10

print(mi_funcion())
print(mi_generador())

g= mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

def mi_generador1():
    x=1
    yield x

    x+=1
    yield x

    x+=1
    yield x

h=mi_generador1()
print(next(h))
print(next(h))
print(next(h))