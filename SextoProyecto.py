#ADMINISTRADOR DE RECETAS
from pathlib import Path
import os
#Saludo de bienvenida, las recetas estan en..., tienes x recetas
#Menu 1.leer receta, 2.crearreceta,3.crearcategoria,4.eliminarreceta,5.eliminarcategoria
#6.finalizarprograma

#Opcion1: elegir categoria, mostrar recetas, elegir receta, leer receta
#Opcion2: elegir categoria, crear nombre, crear contenido
#Opcion 3: nombre categoria, crear categoria
#Opcion 4: elegir categoria, mostrar recetas, elegir receta, eliminar receta
#Opcion 5: elegir categoria, eliminar categoria
#Opcion 6: finalizar la ejecución del codigo
#Hacer el codigo dentro de un while, usar system(cls), usar funciones,



from pathlib import Path
import os

lugar = Path(Path.home(), "Recetas")

def menu():
    print("Este es el menú, selecciona una de las opciones")
    print("Opcion 1: leer receta")
    print("Opcion 2: crear receta")
    print("Opcion 3: crear categoría")
    print("Opcion 4: eliminar receta")
    print("Opcion 5: eliminar categoría")
    print("Opcion 6: finalizar programa")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    print(f"Tienes un total de {contador} recetas")


contar_recetas(lugar)

def inicio():
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        menu()
        eleccion_menu = input("Introduce la opcion 1-6: ")
    return eleccion_menu

def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"{contador}- {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta = input("Elige una categoria: ")
    return lista[int(eleccion_correcta)-1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"{contador}- {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    elecion_receta = "x"
    while not elecion_receta.isnumeric() or int(elecion_receta) not in range(1,len(lista)+1):
        elecion_receta = input("Elige una receta: ")
    return lista[int(elecion_receta)-1]

def leer_receta(receta):
    print(receta.read_text())

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento esa receta ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar != 'v':
        eleccion_regresar = input("\n Presione v para volver al menu: ")

finalizar_programa = False

while not finalizar_programa:
    opcion = inicio()

    if opcion == "1":
        mis_categorias = mostrar_categorias(lugar)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    elif opcion == "2":
        mis_categorias = mostrar_categorias(lugar)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif opcion == "3":
        crear_categoria(lugar)
        volver_inicio()

    elif opcion == "4":
        mis_categorias = mostrar_categorias(lugar)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif opcion == "5":
        mis_categorias = mostrar_categorias(lugar)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif opcion == "6":
        finalizar_programa = True