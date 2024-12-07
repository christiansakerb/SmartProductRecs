import pandas as pd
import mlflow
import os,yaml

def pipelineData_Apriori(df,nivel):
    """" Para la preparación del algoritmo apriori"""
    #Código elimninado por ser de uso privado
    return df_lists,records

def Apriori_Asociaciones_MlFlow(records,params_context,min_support,min_confidence,min_lift,max_length,versionar=True):
    """"Devuelve las reglas de asociación de apriori según las reglas dadas versionado en MLFLOW"""
    # defina el servidor para llevar el registro de modelos y artefactos
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    mlflow.set_tracking_uri(config['host_mlflow'])
    experiment = mlflow.set_experiment("Apriori_rules")
    with mlflow.start_run(experiment_id=experiment.experiment_id) as run:
                
        mlflow.log_param("min_support", min_support)
 
        association_rules = 1 #Código elimninado por ser de uso privado
        association_results = list(association_rules)
        
        mlflow.set_tags({"Tipo_modelo": config['tipo_de_modelo_rec_genr']})
        mlflow.set_tags({"Archivo_tipo": config['tipos_de_archivos_mlflow']['tipo_artefacto']})
        

        #Obtener el id de la corrida de modelo
        #Almacenar modelo

        #Métricas
        mlflow.log_metric("cant_reglas", cant_reglas)
        mlflow.log_metric("combinaciones_detalle", total_combinaciones)

    return association_results
    