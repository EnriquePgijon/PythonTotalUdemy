# Proyecto 4 curso python
# Juego funcional: preguntar al usuario un nombre, nº del 1-100 a ver si lo adivina
# 8 intentos, nº<1 o>100 no esta permitido, si el numero es menor al que
# ha salido, respuesta incorrecta numero menor a el secreto, si lo elije
# mayor, lo mismo pero mayor, y si acierta se le avisa que ha ganado y el numero de intentos usados
#from random import *

#nombre = input("Dime como te llamas")
#intentos = 8
#intentos_U = 0
#numero_S = randint(1, 100)
#print(f"Hola {nombre} empieza el juego")
#while intentos > 0:
 #   numero_U = int(input("Dime el número que crees que es: "))

  #  if (numero_U < 0) or (numero_U > 100):
   #     print("No puedes poner números menores a 0 o mayores a 100")
    #    intentos -= 1
     #   intentos_U += 1

    #elif numero_U < numero_S:
     #   print("Casi, el número secreto es mayor")
      #  intentos -= 1
       # intentos_U += 1

    #elif numero_U > numero_S:
     #   print("Casi, el número secreto es menor")
      #  intentos -= 1
       # intentos_U += 1

    #else:
     #   print("ACERTASTE")
     #   print(f"Has usado un total de: {intentos_U} intentos")
      #  break

    #if(intentos == 0):
     #   print(f"Lo sentimos {nombre}, te has quedado sin intentos, el numero era: {numero_S}")