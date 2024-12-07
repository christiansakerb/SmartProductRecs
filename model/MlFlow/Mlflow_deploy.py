import mlflow
import os,yaml
from mlflow.tracking import MlflowClient
import pandas as pd
import json,joblib,pickle
from tqdm import tqdm
from sdk import add_sdk


def Obtener_Corridas_de_mlflow(tag,config_data):
    """
    Generar todas las corridas de mlflow a la fecha
    """

    mlflow.set_tracking_uri(config_data['host_mlflow'])
    client = MlflowClient()

    #Código elimninado por ser de uso privado
    experiments = client.search_experiments()
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    df_runs = pd.DataFrame(1)
    return df_runs


def Obtener_mejor_modelo_por_experimento(df, medida, run=None, modo='max'):
    """
    Obtiene el modelo con mejor o peor rendimiento según una métrica dada por experimento.
    Si se especifica un run_id, devuelve la información del modelo asociado a ese run.
    
    Parámetros:
        - df: DataFrame con información de los runs y métricas.
        - medida: Nombre de la métrica utilizada para seleccionar el modelo.
        - run: (Opcional) ID del run específico cuyo modelo se desea descargar.
        - modo: (Opcional) 'max' para seleccionar el valor máximo de la métrica, 
                'min' para seleccionar el valor mínimo (por defecto, 'max').
        
    Retorno:
        - DataFrame con el modelo seleccionado por experimento o la información del run especificado.
    """
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    df_run = 1
    return df_run        


def obtener_modelos(df_runs_best_models):    
    """ Para obtener los modelos del MlFlow """
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    Modelos = {}
    for num,run in enumerate(df_runs_best_models['run_id']):
        download_path = 1 #Código elimninado por ser de uso privado        
        artifact_uri = mlflow.get_run(run).info.artifact_uri
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        path = 1 #Código elimninado por ser de uso privado
        tipo_archivo = 1 #Código elimninado por ser de uso privado
        Modelos[df_runs_best_models['Experiment'].iloc[num]] = [download_path,run,path,tipo_archivo] #0 <- ruta descarga, 1 <- cod run , 2<- ruta archivo, 3<- tipo archivo
    return Modelos


def Disponibilizar_modelos_python(Diccionario_de_modelos,config_data,tags):
    """
    Entregar los modelos en un diccionario , Revisa
    """
    
    models_downloaded = {}
    input_schema = {} 
    for nombre_modelo,lista in Diccionario_de_modelos.items(): #0 <- ruta descarga, 1 <- cod run , 2<- ruta archivo, 3<- tipo archivo
        download_path = os.path.join(".", "data", "Pcks_models", f"best_model_{lista[1]}", "artifacts", lista[2])
        add_sdk.modificar_config_yaml("models_info.yml", tags+'_root', download_path) #Almacenar ruta donde se descargó el modelo
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

        if lista[3]==config_data['tipos_de_archivos_mlflow']['tipo_sklearn']: #Código elimninado por ser de uso privado
            #Para traer el modelo
            #Código elimninado por ser de uso privado #<- [2] corresponde al nombre del modelo
            #Para inferir el esquema
            #Código elimninado por ser de uso privado
            inputschema_ind = 1 #Código elimninado por ser de uso privado
            input_schema[lista[2]] = [col.name for col in inputschema_ind] #<- [2] corresponde al nombre del modelo
        else:
            with open(download_path, "rb") as f:
                models_downloaded[lista[2]] = 1 #Código elimninado por ser de uso privado

    return models_downloaded,input_schema

def PythonizarModelos(tags,run,config_data):
    """
    Obtiene modelos previamente entrenados y sus esquemas de entrada asociados basados en las etiquetas proporcionadas.

    Esta función lee un archivo YAML (`models_info.yml`) que contiene información sobre los modelos, como 
    la ubicación del modelo (`root`), el tipo de modelo (`tipo`), y el nombre del modelo (`name`). Dependiendo 
    del tipo de archivo especificado en la configuración (como modelos de scikit-learn o modelos genéricos), 
    carga el modelo correspondiente desde el almacenamiento local y también extrae el esquema de entrada si es posible.

    Args:
        tags (str): Etiqueta que se utiliza para buscar la información del modelo dentro del archivo YAML.
                    Se espera que el archivo YAML tenga claves como `<tags>_root`, `<tags>_tipo` y `<tags>_name` 
                    para obtener la información del modelo.

    Returns:
        tuple: 
            - models_downloaded (dict): Diccionario que contiene el nombre del modelo como clave y el objeto del 
              modelo cargado como valor.
            - input_schema (list): Diccionario de nombres de las columnas del esquema de entrada del modelo si es 
              un modelo MLflow, o una lista vacía si no se puede determinar el esquema.
    
    Raises:
        FileNotFoundError: Si el archivo `models_info.yml` no existe en la ubicación esperada.
        KeyError: Si las claves construidas con el `tags` no existen en el archivo YAML.
        Exception: En caso de que se presente algún error al intentar cargar el modelo o leer el esquema.

    Ejemplo:
        >>> models, schema = PythonizarModelos('modelo_x')
        >>> models
        {'modelo_x': <Modelo cargado>}
        >>> schema
        ['feature1', 'feature2', 'feature3']

    Nota:
        Si el modelo es un archivo de tipo scikit-learn (según la configuración del YAML), 
        se carga usando `mlflow.sklearn.load_model`. Si el tipo es otro, se utiliza `joblib` para cargar el modelo.
    """

    with open('models_info.yml', 'r') as file:
        info_models = yaml.safe_load(file)

    # Comprobar si las claves necesarias existen en el diccionario
    tipo = 'ejemplo'
    name ='ejemplo'
    models_downloaded = {}
    input_schema = {}
    if tipo==config_data['tipos_de_archivos_mlflow']['tipo_sklearn']:
        #Para traer el modelo
        models_downloaded[name] =  1 #Código elimninado por ser de uso privado
        #Para inferir el esquema
        inputschema_ind = 1 #Código elimninado por ser de uso privado
        input_schema[name] = [col.name for col in inputschema_ind] #<- [2] corresponde al nombre del modelo
    
    return models_downloaded,input_schema



def Almacenar_Artefacto_MlFlow(artefacto,config_data,metricas):
    """"Devuelve las reglas de asociación de apriori según las reglas dadas versionado en MLFLOW"""
    # defina el servidor para llevar el registro de modelos y artefactos
    mlflow.set_tracking_uri(config_data['host_mlflow'])
    # registre el experimento
    experiment = mlflow.set_experiment("xxxx")
        #Tags del artefacto        
        #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        #         
        #Obtener el id de la corrida de modelo
        #Almacenar 