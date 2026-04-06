#Turnos de una farmácia
#perfumeria, farmacia, cosmetica, preguntar al cliente a que área se dirige y darle un
#turno que empiece por esa letra, loop
#debe llevar la cuenta de cuantos turnos ha dado para cada área
#Su turno es: turno, espera y sera atendido decoradores...
#numeros.py generadores y decorador
#principal.py funciones import numeros
import numeros

def preguntar():
    print("Bienvenido a Farmacia Python")
    while True:
        print("[P] - Perfumeria"+ "\n"+ "[F] - Farmacia"+ "\n"+ "[C] - Cosmética")
        try:
            mi_rubro= input("Elija su rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Eso no es una opción válida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno=input("Quieres sacar otro turno) [S] [N] ").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una de las opciones")
        else:
            if otro_turno=="N":
                print("Gracias por su visita")
                break

inicio()