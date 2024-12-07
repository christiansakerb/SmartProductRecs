import yaml
from model.Model_Xgboost import TransformData,model_training_testing
from transforms import cleaningData
import pandas as pd
import os
from tqdm import tqdm


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
config_path = os.path.join(project_root, 'configPasillo.yml')
with open(config_path, 'r') as file:
    config_data = yaml.safe_load(file)



def pipelinePrepare_data_train(df,envPasillo,transformacion='total'):
    
    """ 
    Prepara la data para el modelo de categorías distintas
    Recibe el dataframe limpio 

    Devuelve dos dataframes, el primero corresponde a la ultima compra del cliente, y el segundo las compras anteriores
    df1 -> Ultima compra
    df2 -> Compras anteiores

    Tipos transformaciones -> total,parcial
    """

    df_mas_de_1_compra = TransformData.mantiene_ClientesMas1Compra(df)
    #Tipo de transformación a aplicar
    if transformacion=='total':
        df1,df2 = TransformData.Separar_df_en_ult_compra_y_ComprasAnteriores(df_mas_de_1_compra)
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    else:
        print('parcial,total')

        
    # Crear y escribir en el archivo config.yml
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    df1 = df1.map(lambda x: 1 if x > 0 else 0)
    #Código elimninado por ser de uso privado
    return df1,df2 #df_ultima,df_anterior


def Rebalancear_y_organizarDfs(y,X):
    '''Rebalancea las muestras para igualar las clases y devuelve un diccionario con cada y, que tiene una lista con X rebalanceado para esa "y" y su respectiva variable objetivo'''
    Diccionario_y_X = {}
    for col in tqdm(y.columns, desc="Rebalanceando datos"):
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        Diccionario_y_X[col] = 1  
    return Diccionario_y_X

#####
def Obtener_predicciones_testTotal(Resultados_de_modelos,models_mlflow_disponibilizados,input_schema,config_data):
    """Obtener predicicones para evaluar modelo pack"""

    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    for llaves,datas in Resultados_de_modelos['Models'].items():

        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

    metricas = model_training_testing.evaluarModelo(y_pred=y_pred_global,y_true=y_test_global)

    return y_test_global,y_pred_global,metricas



