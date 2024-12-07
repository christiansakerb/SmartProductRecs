import os
import yaml
from model.MlFlow import Mlflow_deploy  

def Pipeline_modelos_disponibles_MLFLOW(tags,metrica_seleccionada,run=None):

    """
    Generar todo el pipeline de descarga de de modelos
    Devuelve modelos en mlflow, dataframe de mejores modelos por experimento
    """

    Diccionario_de_modelos = {}
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    models_mlflow_disponibilizados,input_schema = Mlflow_deploy.Disponibilizar_modelos_python(Diccionario_de_modelos=Diccionario_de_modelos,tags=tags)
    df_runs_best_models =1
    return models_mlflow_disponibilizados,input_schema,df_runs_best_models


def UtilizarModelosEntrenados(tags,metrica_seleccionada=None,run=None,update=True):
    """
    Utiliza modelos entrenados dependiendo de la disponibilidad de la métrica seleccionada.
    Si la métrica seleccionada está presente, se intenta desplegar el modelo con Mlflow.
    Si ocurre un error o no se encuentra el modelo, se llama a la función alternativa para manejar el pipeline de modelos.

    Args:
        tags (str): Etiqueta para buscar la información del modelo.
        metrica_seleccionada (str, opcional): Metrica seleccionada que determinará el flujo de la ejecución.
        run (str, opcional): Identificador de ejecución si se requiere para obtener el mejor modelo.

    Returns:
        dict or object: Dependiendo de si la métrica es válida y si el modelo se encuentra,
                        se devuelve el modelo y los datos relacionados, o se invoca la función alternativa para el pipeline.
    """
    # Si se ha seleccionado una métrica
    if update:
        # Si se ha seleccionado ninguna métrica, se procede a la alternativa directamente
        return Pipeline_modelos_disponibles_MLFLOW(tags=tags, metrica_seleccionada=metrica_seleccionada, run=run)
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
