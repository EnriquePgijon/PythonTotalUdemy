#ANALIZADOR DE TEXTO
#1º Cuantas veces aparecio cada una de las letras
#2ºCuantas palabras hay en total en el texto
#3º Primera y ultima letra del texto
#4º Como queda el texto en inverso
#5º Si la palabra python aparece en el texto
print("A continuacion va a tener que introducir el texto que desee que sea analizado: ")
texto= input("Dime el texto que deseas ingresar: ")
letras=[]
texto=texto.lower()
letras.append(input("Escribe la primera letra: ").lower())
letras.append(input("Escribe la segunda letra: ").lower())
letras.append(input("Escribe la tercera letra: ").lower())

print("\n")
print("Cantidad de letras: ")
letra1=texto.count(letras[0])
letra2=texto.count(letras[1])
letra3=texto.count(letras[2])
print(f"Hemos encontrado {letra1} veces la la letra {letras[0]} en el texto")
print(f"Hemos encontrado {letra2} veces la la letra {letras[1]} en el texto")
print(f"Hemos encontrado {letra3} veces la la letra {letras[2]} en el texto")

print("\n")
print("Cantidad de palabras: ")

palabras=texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")

print("\n")
print("Letra inicial y letra final")
letra_inicio=texto[0]
letra_final=texto[-1]

print(f"La letra inicial es: {letra_inicio} y la letra final es: {letra_final}")

print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido=" ".join(palabras)
print(texto_invertido)

print("\n")
print("Buscar palabra python")
python=palabras.__contains__("python")
print(f"la palabra python {python} si se encuentra en el texto")



