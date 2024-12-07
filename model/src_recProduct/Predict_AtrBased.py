from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from model.src_recProduct import Prods_atrBased
from transforms import CleaningPreds,cleaningData
import pandas as pd
import yaml,joblib,time
from tqdm import tqdm
import numpy as np

def Disimilar(df_productos_tmp,df_clientes_tmp,cod,verbose=True,SoloProductos_Vector=True):
    """ Función para realizar disimilar variables"""
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    if SoloProductos_Vector:
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

    return disimilaridad(tfidf_productos_tmp, tfidf_clientes_tmp)

def procesar_en_bloques(df, chunk_size):
    for i in range(0, len(df), chunk_size):
        yield df[i:i + chunk_size]  # Devuelve los fragmentos uno por uno

def ObtenerDatosProductos(df_recoms,df_prods,cod,atributos,MostrarAntesEliminar,descargar=False):

    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    return df_recoms

def Generar_Recomendaciones_Productos_Atr(df_recomendaciones_Atr,config_data,df_prods_vector,cant_prods,min_prods=10,verbose=True,MostrarAntesEliminar=None,SoloProductos_Vector=True,tiempos=False,descargar=False):
    """Función para generar las recomendaciones basadas en la similitud"""
    #Código elimninado por ser de uso privado
    # #Código elimninado por ser de uso privado
    # #Código elimninado por ser de uso privado    
    resultados = []
    for cod in tqdm(df_recomendaciones_Atr['???'].unique(), desc="Generando recomendaciones",disable=not verbose):
        
        #Generar recomendación para cada sublinea
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

        #Realizar disimilaridad del coseno
        similitudes = Disimilar(df_productos_tmp=df_productos_tmp,df_clientes_tmp=df_clientes_tmp,cod=cod,verbose=False,SoloProductos_Vector=SoloProductos_Vector)
        tiempos and print(f'-- Productos, Madera, Simcoseno {cod} -> {time.time()-t1}') 

        #Obtener los mejores productos :)
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

        df_similitudes['MODELO_PROD']='CSSM'
        

    return pd.concat(resultados,axis=0,ignore_index=True)[config_data['columnas_recom_prods']]


def Generar_Recomendaciones_Productos_RngIRD(df,dfprods,config_data,cant_prods=3,min_prods=10,verbose=True,MostrarAntesEliminar=None):
    """
    Genera recomendaciones de productos basadas en la cercanía entre el rango de XXXXX del cliente
    y el rango de XXXXX del producto, optimizando por ASD. 
        
    Returns:
        DataFrame: Recomendaciones finales con los productos más cercanos.
    """

    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    df_clientes = Prods_atrBased.Generar_codigos_Lineas(df=df,cat='C_CAT',lin='C_LINEA',subl='C_SUBLINEA').copy()
    df_productos = Prods_atrBased.Generar_codigos_Lineas(dfprods).copy()
    resultados = []

    def reemplazar_palabras(texto):
        if pd.isna(texto) or not texto:  # Si el texto es nulo o vacío, devolverlo tal cual
            return texto
        return Diccionario['Diccionario'].get(texto.upper(), texto)
       
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado


    for df_num in tqdm(procesar_en_bloques(df_clientes_tmp, 2000000), desc="Generando recomendaciones ??", disable=not verbose):                
        # Inicializar lista para almacenar resultados
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

    try:
        resultados = pd.concat(resultados,axis=0,ignore_index=True)
        resultados['MODELO_PROD']='RNDS'
        sublineas = resultados['COD_CATEGORIA_TEMP'].unique()
        if verbose:
            print(f'Se han generado {resultados.shape[0]} recomendaciones')
        return resultados[config_data['columnas_recom_prods']]
    except:
        return pd.DataFrame()


def RecomendarBase_REstriccion(df,config_data,df_prods_vector,df_clientes,cant_prods=3,verbose=True,MostrarAntesEliminar=None,descargar=False,prefix=''):
    """Función para generar las recomendaciones basadas en restricciones de clientes"""
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    return df_ini,df


def UnirRecomend_SublProds(df_recomendaciones_Atr,Recomendaciones_con_Prods):
    """Función para añadir recomendaciones de XSXS a las de PDS"""
    #Código elimninado por ser de uso privado
    # #Código elimninado por ser de uso privado
    # #Código elimninado por ser de uso privado
    # #Código elimninado por ser de uso privado    
    df_recomendaciones_Atr = df_recomendaciones_Atr.merge(Recomendaciones_con_Prods,how='left',on=['N_IDE','COD_CATEGORIA_TEMP'])
    return df_recomendaciones_Atr


def UnirRecomnedacionesRestricciones_Predichas(df,df_original,df_restriccion,verbose=True,rellenar_cupo_cero=True,sep=';'): 
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    df_restriccion = CleaningPreds.Ajustar_recomendacionesProdsCupo(df_restriccion,sep=sep)
    df = cleaningData.GenerarColumna_siNoExiste(df=df,columnas=df_restriccion.columns,valor_predeterminado='-')
    
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    df = UnirRecomend_SublProds(df_original,df) 
    
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    return df




def AgregarInfo_ModeloProd(df,sep):
    '''
    Lógica para renombrar los modelos con información relevante del cupo
    NC -> Cliente sin SDDS, se entrega recomendación original
    CI -> Cliente con SDDS insuficiente para una compra, mantiene vacio
    RC -> Cliente con recomendaciones basadas en su SDDS
    '''
       # Lógica para actualizar la columna MODELO_PROD según las condiciones
    df['MODELO_PROD'] = np.where(df['SDDS'] == 0, df['MODELO_PROD'] + sep + "NC",df['MODELO_PROD'])
    df['MODELO_PROD'] = np.where((df['SDDS'] > 0) & (df['COD_APLICABLE'].isin(['-', ''])),df['MODELO_PROD'] +  sep + "CI",df['MODELO_PROD'])
    df['MODELO_PROD'] = np.where((df['SDDS'] > 0) & (~df['COD_APLICABLE'].isin(['-', ''])),df['MODELO_PROD'] + sep + "RC",df['MODELO_PROD'])
    