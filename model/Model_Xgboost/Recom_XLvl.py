from model.Model_Xgboost import TransformData,model_training_testing
from transforms import cleaningData,CleaningPreds
import os,yaml
import pandas as pd
from tqdm import tqdm
import datetime,time

def Organizar_df_para_predict_xgboost(df,input_schema,config_data):
    """ Entrega X, las cedulas y el vector de compras de clientes """

    input_schema = list(set().union(*input_schema.values()))
    df_vectores = cleaningData.Obtener_vector_de_clientes_en_col(df,config_data['Nivel_general'])    
    df = TransformData.pipelinePrepare_VectorizeData(df,config_data['lvl_xgboost'])
    
    #Crear columnas si no existen
    df = Reorganizar_columnas(df,input_schema)
    
    return df[input_schema],df[input_schema].index,df_vectores


def Reorganizar_columnas(df, features):
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    return df

def Generar_columnas_distintos_dfs(df_principal,df_a_rellenar):
    for col in df_principal.columns:
        if col not in df_a_rellenar.columns:
            df_a_rellenar[col] = 0  

    return df_a_rellenar


def Recomendar_xgboost_lvl(Models,input_schema,data,n_cliente,config_data,df_vector_compras,MostrarAntesEliminar=None,tope=3,confianza_min=0.5,verbose=True,tiempos=False):
    """Generar predicciones de xgboost

    Ejemplo de uso:
    >>> Recomendar([1, 2, 3])
    Procesando datos: [1, 2, 3]

    """
    #Df_vacío a rellenar con predicciones
    df_total = pd.DataFrame()#columns=config_data['Datos_de_respuesta']
    #Código elimninado por ser de uso privado

    for key in tqdm(Models.keys(), desc="Procesando modelos XGBoost",disable=not verbose):

        #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado

     #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    df_total = Generar_columnas_distintos_dfs(df_principal=df_total,df_a_rellenar=df_total)
    df_total = df_total[config_data['Datos_Preparados']]

    df_total = CleaningPreds.Limpiar_predicciones(df_total,col_recomendacion='C_CATEGORIA',config_data=config_data,col_lista_compras='ULTIMA_COMPRA',MostrarAntesEliminar=MostrarAntesEliminar,col_grupo=['N_IDE','C_CATEGORIA'],verbose=verbose,tiempos=tiempos)
    df_total = CleaningPreds.Mantener_MejoresPredicciones(df_total,tope=tope,MostrarAntesEliminar=MostrarAntesEliminar,verbose=verbose)

    return df_total

def Predecir_XgboostParalelo(clientes,clientes_index,modelos,input_schema):
    from concurrent.futures import ThreadPoolExecutor
    class Modelo:
        def __init__(self, nombre,modelo_entrenado,columnas_requeridas):
            self.nombre = nombre
            self.modelo_entrenado = modelo_entrenado
            self.columnas_requeridas = columnas_requeridas
        
    # Crear 10 modelos simulados    
#    modelos = [Modelo(f"{key}") for key in modelos.keys()]
    modelos_instanciados = [Modelo(nombre=key, modelo_entrenado=modelos[key], columnas_requeridas=input_schema[key]) for key in modelos.keys()]

    # Función para predecir con un solo modelo
    def predecir_con_modelo(modelo_instancia):
        return modelo_instancia.modelo_entrenado.predict(clientes[modelo_instancia.columnas_requeridas])

    t1 = time.time()
    with ThreadPoolExecutor(max_workers=len(modelos_instanciados)) as executor:
            # Ejecutamos la predicción en paralelo para cada modelo
            resultados = list(executor.map(predecir_con_modelo, modelos_instanciados))
    print( time.time()-t1)

    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    
    return df_resultados
