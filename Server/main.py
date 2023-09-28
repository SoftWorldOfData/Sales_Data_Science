import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

Dataset = os.getenv("Amazon")

amazon = pd.read_csv(Dataset)

amazon.info()

Dataset_Copy = amazon.copy()

def EDA():

    amazon.head()

    describe = amazon.describe()

    print('descripcion del dataset', describe)

    print('primeras filas del dataset', amazon)

def Categoria():

    return None


def Clean_Data():

    valores_faltantes = Dataset_Copy.isna().sum()

    print(valores_faltantes)

    print("Estamos viendo rating_count", Dataset_Copy["rating_count"].head())

    print("vamos a ver la descripcion de rating_count", Dataset_Copy["rating_count"].describe())

Clean_Data()