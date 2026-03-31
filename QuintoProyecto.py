#Programa el ahorcado
#palabra secreta, muestra al jugador la cantidad de caracteres, en guiones que tiene la palabra
#Si adivina alguna letra, se muestra en el lugar correspondiente, de lo contrario
#El jugador perderá una vida, tiene 6 vidas, si el jugador adivina la palabra antes gana
#import choice, funciones para pedirletra,validarletra,chequearletra,haganado.
from random import choice
print("Bienvenido a el juego del ahorcado")
palabras = [
    "elefante", "mariposa", "cocodrilo", "pingüino", "murciélago",
    "camaleón", "albatros", "rinoceronte", "salamandra", "flamenco",
    "volcán", "glaciar", "arcoíris", "tormenta", "cascada",
    "acantilado", "manantial", "huracán", "sabana", "pantano",
    "paraguas", "calculadora", "termómetro", "telescopio", "microscopio",
    "escalera", "chimenea", "almohada", "linterna", "calendario",
    "alcachofa", "frambuesa", "berenjena", "calabacín", "mandarina",
    "espárrago", "cangrejo", "mejillón", "zanahoria", "aguacate",
    "biblioteca", "aeropuerto", "cementerio", "laboratorio", "planetario",
    "acuario", "monasterio", "anfiteatro", "invernadero", "mausoleo",
    "arqueólogo", "carpintero", "fontanero", "arquitecto", "astronauta",
    "bombero", "periodista", "veterinario", "electricista", "cartógrafo",
    "ferrocarril", "extraterrestre", "supermercado", "electrodoméstico",
    "biodiversidad", "circunferencia", "murmullo", "zigzag", "xilófono",
]
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def palabra_aleatoria(lista_palabras):
    palabra_elegida= choice(lista_palabras)
    letras_unicas= len(set(palabra_elegida))
    return palabra_elegida,letras_unicas
def pedir_letra():
    es_valida=False
    abecedario='abcdefghijklmnñopqrstvwxyz'
    while not es_valida:
        letra_elegida=input('elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print("No has elegido una letra correcta")
    return letra_elegida
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin=False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias+=1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas-=1

    if vidas==0:
        fin=perder()
    elif coincidencias==letras_unicas:
        fin=ganar(palabra_oculta)

    return vidas, fin,coincidencias

def perder():
    print("Te has quedado sin vidas, has perdido")
    print(f"La palabra oculta era {palabra}")

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades has encontrado la palabra")
    return True

palabra, letras_unicas= palabra_aleatoria(palabras)

while not juego_terminado:
    print('\n'"****************************************"'\n')
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: "+ "-".join(letras_incorrectas))
    print(f"Vidas {intentos}")
    print('\n'"****************************************"'\n')
    letra= pedir_letra()
    intentos,terminado,aciertos=chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado=terminado


