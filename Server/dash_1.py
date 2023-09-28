import matplotlib.pyplot as plt
import numpy as np
from main import Dataset_Copy
import re

# product_name = Dataset_Copy["product_name"]

# price = Dataset_Copy["actual_price"]


# Genera algunos datos de ejemplo (reemplaza esto con tus propios datos)
# datos = np.random.randn(1000)  # Datos aleatorios para el ejemplo

def Diagrama_Dispersion():

    x = np.random(100)

    y = np.random(100)

    plt.scatter(x, y)


    plt.title('Diagrama de Dispersión')
    plt.xlabel('Variable X')
    plt.ylabel('Variable Y')

    # Mostrar el gráfico
    plt.show()

def Histogram():

    # Dataset_Copy["discounted_price"] = Dataset_Copy["discounted_price"].str.replace('₹', '').astype(float)
    # Dataset_Copy['discounted_price'] = Dataset_Copy['discounted_price'].str.replace(",", "").astype(int)

    # Supongamos que 'df' es tu DataFrame y 'discounted_price' es la columna que contiene los precios con el símbolo de rupia
    # Dataset_Copy['discounted_price'] = Dataset_Copy['discounted_price'].str.replace('₹', '').astype(int)

    # Supongamos que 'df' es tu DataFrame y 'discounted_price' es la columna que contiene los precios con el símbolo de rupia
    # Eliminar todos los caracteres no numéricos usando una expresión regular
    Dataset_Copy['discounted_price'] = Dataset_Copy['discounted_price'].apply(lambda x: int(re.sub(r'\D', '', x)))

    # Crea el histograma
    plt.hist(Dataset_Copy["discounted_price"], bins=20, color='blue', alpha=0.7)
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos')

    # Muestra el histograma
    plt.show()

Histogram()