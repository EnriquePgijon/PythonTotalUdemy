#Script dia 5

#MÉTODOS, AYUDA Y DOCUMENTACIÓN
#dic={'clave 1':100,'clave 2':500}
#Mediante la notación de punto podemos ver los métodos disponibles para cada objeto
#dic.popitem()

#FUNCIONES
#Estructura de la funcion def es la palabra clave
#def nombre(parametros):

#def saludar_persona(nombre):
  #  '''
  #  Esta funció sirve para saludar a las personas
   # '''
 #   print("Hola " + nombre)

#saludar_persona('Fernando')

#RETURN
#def multiplicar(numero1,numero2):
 #   return numero1*numero2
#print(multiplicar(2,3))
#Imprimir muestra en pantalla, return tiene un resultado guardado para uso posterior

#FUNCIÓNES DINÁMICAS
#def chequear_3_cifras(numero):
 #   return numero in range(100,1000)

#suma=586+490
#resultado=chequear_3_cifras(suma)
#print(resultado)

#def chequear_3_cifras(lista):
 #   lista_3_cifras=[]
  #  for n in lista:
   #     if n in range(100,1000):
    #        lista_3_cifras.append(n)
     #   else:
      #      pass
    #return lista_3_cifras
#resultado=chequear_3_cifras([55,999,600])
#print(resultado)

#EJEMPLO DE FUNCIÓN

#precios_cafe=[('capuccino',1.5),('expresso',2.5),('Moka',1.9)]
#for cafe,precio in precios_cafe:
 #   print(precio*0.45)

#def cafe_mas_caro(lista_precios):
 #   precio_mayor=0
  #  cafe_mas_caro=''

   # for cafe,precio in lista_precios:
    #    if precio>precio_mayor:
     #       precio_mayor=precio
      #      cafe_mas_caro=cafe
       # else:
        #    pass
    #return(cafe_mas_caro,precio_mayor)
#print(cafe_mas_caro(precios_cafe))


#INTERACCIÓN ENTRE FUNCIONES
#from random import *
#lista inicial
#palitos=['-','--','---','----']

#Mezclar palitos
#def mezclar(lista):
 #   shuffle(lista)
  #  return lista

#print(mezclar(palitos))

#pedirle intento
#def probar_suerte():
   # intento=''
  #  while intento not in ['1','2','3','4']:
    #    intento=input("Elige un numero del 1 al 4: ")

 #   return int(intento)
#Comprobar intento
#def chequear_intento(lista,intento):
 #   if lista[intento-1]=='-':
  #      print("A lavar los platos")
   # else:
    #    print("esta vez te has salvado")
    #print(f"Te ha tocado {lista[intento-1]}")


#palitos_mezclados=mezclar(palitos)
#seleccion= probar_suerte()
#chequear_intento(palitos_mezclados,seleccion)


#ARGUMENTOS INDEFINIDOS *args
#Permite poner muchos argumentos en funciones que lo necesitemos
#def suma(*args):
    #return sum(args)
   # total=0
   # for arg in args:
    #    total+=arg
    #return total

#print(suma(5,6,8))

#ARGUMENTOS INDEFINIDOS *kwargs
#Sirven para conjuntos clave valor solamente
#def prueba(num1,num2,*args,**kwargs):
 #   print(f"El primer valor es: {num1}")
  #  print(f"El segundo valor es: {num2}")

   # for arg in args:
    #    print(f"arg = {arg}")


    #for clave,valor in kwargs.items():
     #   print(f"{clave} = {valor}")

#args=[100,200,300,400]
#kwargs={'x':'uno','y':'dos'}
   # print(type(kwargs))

#prueba(15,50,*args,**kwargs)

#PROBLEMAS PRÁCTICOS
#1º
#def devolver_distintos(int1, int2, int3):
 #   numeros = [int1, int2, int3]
  #  suma = sum(numeros)

   # if suma > 15:
    #    return max(numeros)
    #elif suma < 10:
     #   return min(numeros)
    #else:                          # entre 10 y 15
     #   return sorted(numeros)[1]  # el valor del medio
#2º
#def ordena(palabra):
 #   ordenado=[]
  #  for i in palabra:
   #     if i not in ordenado:
    #      ordenado.append(i)

    #ordenado.sort()
    #return ordenado

#print(ordena('entretenido'))

#3º
#def indefinida(*args):
 #   numeros=[]
  #  for arg in args:
   #     numeros.append(arg)
    #for i in numeros:
     #   if numeros.count(0)>1:
      #      return True

#print(indefinida(5,4,5,3,2,64,9,0))

#4º
#def contar_primos(num):
 #   contador_p = 0
  #  for i in range(2, num + 1):
   #     divisores = 0
    #    for j in range(1, i + 1):
     #       if i % j == 0:
      #          divisores += 1
       # if divisores == 2:
        #    contador_p += 1
   # return contador_p

#print(contar_primos(10))
#print(contar_primos(5))