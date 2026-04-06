# CLASES
#class Pajaro:
    # ATRIBUTOS de clase
 #   alas = True

    # CONSTRUCTOR
#    def __init__(self, color, especie):
 #       self.color = color
  #      self.especie = especie

    # MÉTODOS
   # def piar(self):
    #    print("pio, mi color es {}".format(self.color))

    #def volar(self, metros):
     #   print(f"El pajaro ha volado {metros} metros")
      #  self.piar()


# INSTANCIAS
#mi_pajaro = Pajaro("negro", "tucán")

#print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
#print(Pajaro.alas)
#print(mi_pajaro.alas)

#piolin = Pajaro("amarillo", "canario")
#piolin.piar()
#piolin.volar(89)

#TIPOS DE MÉTODOS
#Metodos de instancia usados hasta ahora self
#afectan al self, pueden acceder y modificar el objeto
   # def pintar_negro(self):
  #      self.color="negro"
 #       print(f"Ahora el pajaro es: {self.color}")
#piolin.alas = False
#metodos de clase @classmethod se pone cls no self
    #@classmethod
   # def poner_huevos(cls, cantidad):
  #      print(f"Puso {cantidad} huevos")
 #       cls.alas=True

#Pajaro.poner_huevos(3)
#metodos estaticos @staticmethod no aceptan self ni cls como parámetro
   # @staticmethod
  #  def mirar():
 #       print("El pajaro mira")
#Pajaro.mirar()

#METODOS ESPECIALES son todos los que tienen __ en su llamada
