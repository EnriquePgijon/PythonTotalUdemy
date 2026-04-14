#PROGRAMAR UN EXTRACTOR DE DATOS WEB

#EXTRAER EL TITULO DE UNA PAGINA WEB
import bs4
import requests

resultado= requests.get("https://www.escueladirecta.com/courses")
#Devuelve lo que se encuentre en el nombre de esa etiqueta
sopa= bs4.BeautifulSoup(resultado.text,"lxml")
print(sopa.select("title")).gettext()#Quita las etiquetas y devuelve solo el texto

#EXTRAER LOS ELEMENTOS DE UNA CLASE COMPLETA
columna_lateral=sopa.select(".content p")
for p in columna_lateral:
    print(p.getText())

#EXTRAER IMAGENES
imagenes= sopa.select(".course-box.image")
for imagen in imagenes:
    print(imagen)

imagen_curso_1= requests.get(imagenes)

f=open("mi_imagen.jpg","wb")
f.write(imagen_curso_1.content)
f.close()

#TOSCRAPE.COM
#como explorar diferentes páginas de un sitio web

url="https://books.toscrape.com/cataloque/page-{}.html"
for n in range(1,11):
    print(url.format(n))

#IDENTIFICAR CONDICIONES DE EXTRACCIÓN
resultado= requests.get(url.format("1"))
sopa=bs4.BeautifulSoup(resultado.text,"lxml")
libros= sopa.select(".product_pod")
ejemplo=libros[0].select("a")[1]["title"]
print(ejemplo)
#COMBINAR ITEMS BUSCADOS
# lista de titulos con 4 o 5 estrellas
titulos_rating_alto=[]

#iterar paginas
for pagina in range(1,51):
    #crear sopa en cada pagina
    url_pagina=url.format(pagina)
    resultado= requests.get(url_pagina)
    sopa=bs4.BeautifulSoup(resultado.text,"lxml")
    #seleccionar datos de los libros
    libros= sopa.select(".product_pod")
    #iterar libros
    for libro in libros:
        #chequear 4 o 5 estrellas
        if len(libro.select(".star-rating.Four"))!=0 or len(libro.select(".star-rating.Five"))!=0:
            #guardar titulo en variable
            titulo_libro= libro.select("a")[1]["title"]
            #agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)


#ver libros de 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)