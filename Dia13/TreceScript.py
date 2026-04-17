# ASISTENTE DE VOZ

# Instalar bibliotecas
# pyttsx3, SpeechRecognition, pywhatkit, yfinance, pyjokes

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# TRANSFORMAR VOZ EN TEXTO
def transformar_audio_en_texto():
    r = sr.Recognizer()

    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("ya puedes hablar")
        audio = r.listen(origen)

        try:
            pedido = r.recognize_google(audio, language="es-ar")
            print("Dijiste: " + pedido)
            return pedido

        except sr.UnknownValueError:
            print("ups, no entendi")
            return "sigo esperando"

        except sr.RequestError:
            print("ups, no entendi")
            return "sigo esperando"

        except:
            print("ups, algo ha salido mal")
            return "sigo esperando"


# TRANSFORMAR TEXTO EN VOZ
def hablar(mensaje):
    engine = pyttsx3.init()
    engine.say(mensaje)
    engine.runAndWait()


# CONFIGURAR VOCES
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)


# INFORMAR EL DIA
def pedir_dia():
    dia = datetime.date.today()
    dia_semana = dia.weekday()

    calendario = {
        0: "lunes",
        1: "martes",
        2: "miercoles",
        3: "jueves",
        4: "viernes",
        5: "sabado",
        6: "domingo"
    }

    hablar(f"Hoy es: {calendario[dia_semana]}")


# INFORMAR LA HORA
def pedir_hora():
    hora = datetime.datetime.now()
    mensaje = f"En este momento son las: {hora.hour} con {hora.minute} minutos y {hora.second} segundos"
    print(mensaje)
    hablar(mensaje)


# SALUDO INICIAL
def saludo_inicial():
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos dias"
    else:
        momento = "Buenas tardes"

    hablar(f"{momento}, soy Helena, tu asistente personal. Por favor dime en que te puedo ayudar")


# FUNCION PRINCIPAL
def pedir_cosas():
    saludo_inicial()
    comenzar = True

    while comenzar:
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("Okey, estoy abriendo youtube")
            webbrowser.open('https://www.youtube.com/')
            continue

        elif "abrir navegador" in pedido:
            hablar("Okey, estoy abriendo navegador")
            webbrowser.open('https://www.google.com/')
            continue

        elif "que dia es hoy" in pedido:
            pedir_dia()
            continue

        elif "que hora es" in pedido:
            pedir_hora()
            continue

        elif "buscar en wikipedia" in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("buscar en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(resultado)
            continue

        elif "buscar en internet" in pedido:
            hablar("ya mismo lo hago")
            pedido = pedido.replace("buscar en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue

        elif "reproducir" in pedido:
            hablar("Buena idea, ya empiezo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue

        elif "broma" in pedido:
            hablar(pyjokes.get_joke(language="es"))
            continue

        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "AAPL", "amazon": "AMZN", "google": "GOOGL"}

            try:
                accion_buscada = yf.Ticker(cartera[accion])
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre, el precio de {accion} es {precio_actual} $")
            except:
                hablar("perdon, pero no la he encontrado")

            continue

        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


# EJECUTAR
pedir_cosas()