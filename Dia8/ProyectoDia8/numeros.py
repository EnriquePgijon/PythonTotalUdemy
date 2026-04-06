#Turnos de una farmácia
#perfumeria, farmacia, cosmetica, preguntar al cliente a que área se dirige y darle un
#turno que empiece por esa letra, loop
#debe llevar la cuenta de cuantos turnos ha dado para cada área
#Su turno es: turno, espera y será atendido decoradores...
#numeros.py generadores y decorador
#principal.py funciones import numeros

def numeros_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

p=numeros_perfumeria()
f=numeros_farmacia()
c=numeros_cosmetica()

def decorador(rubro):
    print("\n"+ "*"*23)
    print("Su numero es: ")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("*"*23 +"\n")