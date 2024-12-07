import pandas as pd
import random,sys
import string
import inspect



def filtrar_filas_por_valor(df, columna, valor, c_subl=None):
    """
    Filtra las filas de un DataFrame donde una columna contiene un valor específico.

    Args:
        df (pd.DataFrame): El DataFrame a filtrar.
        columna (str): El nombre de la columna donde buscar el valor.
        valor (str): El valor exacto a buscar en la columna.

    Returns:
        pd.DataFrame: Un nuevo DataFrame con las filas filtradas.
    """
    filtro = df[columna].str.contains(rf'\b{valor}\b', na=False)
    df = df[filtro][['N_IDE','SKUS_COMPRAS','C_CATEGORIA','C_SUBLINEA','MODELO','COD']]
    if c_subl is not None:
        df = df[df['C_SUBLINEA']==c_subl]
    return df


import yaml

def modificar_config_yaml(ruta_config, clave, nuevo_valor):
    # Leer el archivo de configuración
    with open(ruta_config, 'r') as file:
        config = yaml.safe_load(file)
        config[clave] = nuevo_valor
    
    # Guardar los cambios de vuelta al archivo YAML
    with open(ruta_config, 'w') as file:
        yaml.safe_dump(config, file)


# Función para generar un código alfanumérico aleatorio
def generar_codigo(longitud=16):
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    return ejemplo
# Agregar una nueva columna con códigos aleatorios al DataFrame

def Medir_tamañoVariable(df,nombre_variable):
    print(f'Espacio de {nombre_variable} en memoria usado en MB-> {sys.getsizeof(df)/(1024**2):.2f}, con tamaño {df.shape}')
