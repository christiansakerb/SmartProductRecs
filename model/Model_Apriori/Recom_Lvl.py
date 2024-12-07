import pandas as pd
import os, yaml
from transforms import cleaningData,CleaningPreds
import datetime
from tqdm import tqdm


def Generar_recomendaciones_sublineas(clientes,Reglas_pd,config_data,MostrarAntesEliminar=None,tope=3,verbose=True):
    Clientes_vectorizados = cleaningData.Obtener_vector_de_clientes_en_col(df=clientes,nivel=config_data['Nivel_general'])
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    tqdm.pandas(desc="Generando Recomendaciones Apriori",disable=not verbose)
    # Función para verificar coincidencias de reglas
    def verificar_reglas(ultima_compra):
        # Lista para almacenar índices de coincidencia
        indices_coincidentes = []        
        return indices_coincidentes

    #verificar_reglas(Clientes_vectorizados.head(5),Reglas_pd[['antecedent_list']].head(5))
    Clientes_vectorizados['REGLAS_COINCIDENTES'] = Clientes_vectorizados['ULTIMA_COMPRA'].progress_apply(verificar_reglas)

    #Traemos los datos aplicables
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    #Clientes   
    Clientes_vectorizados_exploded = Clientes_vectorizados_exploded[config_data['Datos_Preparados']]
    
    #Código elimninado por ser de uso privado   
    df_total = CleaningPreds.Limpiar_predicciones(Clientes_vectorizados_exploded,col_recomendacion='C_CATEGORIA',
                                                 col_lista_compras='ULTIMA_COMPRA',config_data=config_data,
                                                 col_grupo=['N_IDE','C_CATEGORIA'],MostrarAntesEliminar=MostrarAntesEliminar,verbose=verbose
                                                 ) #
    
    df_total = CleaningPreds.Mantener_MejoresPredicciones(df_total,tope=tope,MostrarAntesEliminar=MostrarAntesEliminar,verbose=verbose)

    return df_total 