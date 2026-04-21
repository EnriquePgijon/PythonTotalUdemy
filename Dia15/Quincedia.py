# ══════════════════════════════════════════════════════════════════════════════
# PROGRAMA: INTRODUCCIÓN A MACHINE LEARNING CON PYTHON
# Librerías: NumPy, Pandas, Matplotlib
# Entorno recomendado: Google Colab
# ══════════════════════════════════════════════════════════════════════════════


# ── SECCIÓN 1: VARIABLES Y FUNCIONES BÁSICAS ──────────────────────────────────

nombre = 'Federico'
edad = 45

def mostrar_nombre(persona):
    # Muestra un saludo con el nombre recibido
    print("Hola " + persona)  # CORRECCIÓN: faltaba espacio tras "Hola"

mostrar_nombre("Miguel")


# ── SECCIÓN 2: NUMPY — ARRAYS Y OPERACIONES ───────────────────────────────────

import numpy as np
import pandas as pd

# Crear arrays de 1, 2 y 3 dimensiones
array_unidim = np.array([1, 2, 3, 4, 5])
array_bidim  = np.array([[1, 2, 3], [4, 5, 6]])
array_tridim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Inspeccionar propiedades: forma, dimensiones, tipo de dato, tamaño y tipo Python
print(array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim))
print(array_bidim.shape,  array_bidim.ndim,  array_bidim.dtype,  array_bidim.size,  type(array_bidim))
print(array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_tridim))

# Convertir array a DataFrame de Pandas
datos = pd.DataFrame(array_bidim)

# Arrays especiales
unos  = np.ones((4, 3))          # Array relleno de 1s con forma (4, 3)
ceros = np.zeros((2, 4, 3))      # Array relleno de 0s con forma (2, 4, 3)

# Rangos y arrays aleatorios
array_1 = np.arange(0, 100, 5)           # Valores de 0 a 100 en pasos de 5
array_2 = np.random.randint(0, 10, (2, 5))  # Enteros aleatorios entre 0 y 9
array_3 = np.random.random((3, 5))          # Flotantes aleatorios en [0, 1)

# Fijar semilla para que los resultados sean reproducibles
np.random.seed(27)
array_4 = np.random.randint(0, 10, (3, 5))

# Operaciones de indexado y slicing
np.unique(array_4)   # Valores únicos del array
array_4[1]           # Segunda fila
array_4[:2]          # Primeras dos filas
array_2[:2, :2]      # Submatriz de las primeras 2 filas y 2 columnas

# Operaciones aritméticas entre arrays (deben tener la misma forma)
array_5 = np.random.randint(0, 10, (3, 4))
array_6 = np.ones((3, 4))
array_5 + array_6    # Suma elemento a elemento

# CORRECCIÓN: np.ones() recibe una tupla, no dos argumentos separados
# INCORRECTO: array_7 = np.ones(4, 3)
array_7 = np.ones((4, 3))
array_8 = np.ones((4, 3))
array_8 - array_7    # Resta elemento a elemento

# Multiplicación, potencia y raíz cuadrada
array_9  = np.random.randint(1, 5, (3, 3))
array_10 = np.random.randint(1, 5, (3, 3))
array_9 * array_10   # Multiplicación elemento a elemento
array_9 ** 2         # Elevar al cuadrado
np.sqrt(array_10)    # Raíz cuadrada

# Estadísticas básicas
array_9.mean()       # Media
array_9.max()        # Máximo
array_9.min()        # Mínimo

# Cambiar la forma del array (reshape) y transponer
array_11 = array_9.reshape((9, 1))
array_11.T           # CORRECCIÓN: .T es una propiedad, no un método → sin paréntesis

# Arrays booleanos: comparaciones
array_12 = array_9 > array_10   # Devuelve True/False por elemento
array_12.dtype                   # dtype será bool
array_9 > 2                      # Comparación escalar

# Ordenar un array
np.sort(array_9)


# ── SECCIÓN 3: PANDAS — SERIES Y DATAFRAMES ───────────────────────────────────

import pandas as pd

# Crear Series (columnas individuales)
# CORRECCIÓN: pd.Series() requiere paréntesis y los valores entre corchetes
numeros  = pd.Series([1, 2, 3, 4, 56, 3, 5])
numeros.mean()   # Media de la serie
numeros.sum()    # Suma de la serie

colores     = pd.Series(["rojo", "amarillo", "verde"])
tipo_autos  = pd.Series(["Sedán", "SUV", "Pick up"])

# Crear DataFrame combinando varias Series
# CORRECCIÓN: la sintaxis del diccionario estaba mal (faltaban llaves de cierre)
tabla_autos = pd.DataFrame({"Tipo de auto": tipo_autos, "Color": colores})
tabla_autos


# ── SECCIÓN 4: CARGAR Y EXPLORAR DATOS DESDE GOOGLE DRIVE ────────────────────

#from google.colab import drive
#drive.mount('/content/drive')   # Montar Google Drive en Colab

# CORRECCIÓN: el método correcto es read_csv, no read_cdv
ventas_autos = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ventas-autos.csv')

# Guardar el DataFrame de vuelta a CSV
ventas_autos.to_csv('/content/drive/MyDrive/Colab Notebooks/ventas-autos.csv')

# Exploración básica del DataFrame
ventas_autos.dtypes        # Tipo de dato de cada columna
ventas_autos.describe()    # Estadísticas descriptivas (media, std, min, max…)
ventas_autos.info()        # Información general (tipos, valores nulos)
ventas_autos.columns       # Nombres de las columnas
len(ventas_autos)          # Número de filas

# Primeras y últimas filas
ventas_autos.head()        # Primeras 5 filas (por defecto)
ventas_autos.head(7)       # Primeras 7 filas
ventas_autos.tail(3)       # Últimas 3 filas

# Acceso a filas por etiqueta e índice
ventas_autos.loc[3]              # Fila con etiqueta 3
ventas_autos.iloc[[3, 7, 9]]    # Filas en las posiciones 3, 7 y 9

# Acceso y filtrado de columnas
ventas_autos['kilometraje']                         # Columna completa
ventas_autos["kilometraje"].mean()                  # Media del kilometraje
ventas_autos[ventas_autos["kilometraje"] > 100000]  # Filtrar por condición

# Tablas cruzadas y agrupaciones
pd.crosstab(ventas_autos['Fabricante'], ventas_autos["Puertas"])
ventas_autos.groupby(["Fabricante"]).mean()   # Media de cada grupo

# Limpieza de la columna de precios (quitar símbolos y convertir a número)
ventas_autos["Precio (USD)"] = ventas_autos["Precio (USD)"].str.replace(r"[\,\$\.]", "", regex=True)
ventas_autos["Precio (USD)"] = ventas_autos["Precio (USD)"].astype(int) / 100
ventas_autos


# ── SECCIÓN 5: MATPLOTLIB — VISUALIZACIÓN DE DATOS ────────────────────────────

#import matplotlib.pyplot as plt
#%matplotlib inline   # Mostrar gráficos en el notebook

# Gráfico de línea simple
a = [1, 5, 6, 3, 15]
plt.plot(a)

# Gráfico de línea con datos calculados (y = x²)
x = list(range(101))
y = [numero ** 2 for numero in x]   # List comprehension (más limpio que el bucle)
plt.plot(x, y)

# Gráfico con figura y ejes explícitos, con título y etiquetas
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(
    title="Gráfico de casos de COVID-19 en Latam",
    xlabel="Días",
    ylabel="Casos confirmados"
)
fig.savefig("/ejemplo-grafico-covid.png")   # Guardar la figura en disco

# Gráfico de dispersión (scatter)
# CORRECCIÓN: el módulo se llama numpy, no numpu
x_1 = np.linspace(0, 100, 20)
y_1 = x_1 ** 2

fig, ax = plt.subplots()
ax.scatter(x_1, y_1)

# Gráfico de dispersión de la función seno
x_2 = np.linspace(-10, 10, 100)
y_2 = np.sin(x_2)

fig, ax = plt.subplots()
ax.scatter(x_2, y_2)

# Gráfico de barras verticales
comidas = {"lasaña": 350, "sopa": 150, "roast beef": 650}

fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())
# CORRECCIÓN: la sintaxis de ax.set() estaba mal (paréntesis mal colocados)
ax.set(title="Precios de comidas", ylabel="Precio", xlabel="Comida")

# Gráfico de barras horizontales
# CORRECCIÓN: los argumentos deben pasarse separados, no anidados en un solo paréntesis
fig, ax = plt.subplots()
ax.barh(list(comidas.keys()), list(comidas.values()))

# Histograma
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x)

# Subplots: cuadrícula de 4 gráficos en 2 filas × 2 columnas
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

ax1.plot(x_1, y_1)                           # Línea y = x²
ax2.scatter(x_2, y_2)                        # Dispersión del seno
ax3.bar(comidas.keys(), comidas.values())    # Barras de precios
ax4.hist(np.random.randn(1000))             # Histograma de distribución normal

# Cambiar el estilo visual de los gráficos
plt.style.available          # Ver estilos disponibles
plt.style.use('seaborn-whitegrid')   # Aplicar estilo limpio con grilla

