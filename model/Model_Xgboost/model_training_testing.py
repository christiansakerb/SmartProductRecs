from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.multiclass import OneVsRestClassifier
import xgboost
from sklearn.metrics import  precision_score, recall_score, f1_score, accuracy_score
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from tqdm import tqdm

import os,yaml


def Versionar_MlFlow(model,llave,metricas,config,params,nuevo_umbral,input_example,params_context):
    #Generación de modelos
    mlflow.set_tracking_uri(config['host_mlflow'])
    # registre el experimento
    experiment = mlflow.set_experiment("MdXboost"+llave)
    
    with mlflow.start_run(experiment_id=experiment.experiment_id) as run:    

        mlflow.log_params({"n_estimators": params['n_estimators']})
        mlflow.log_params({"max_depth": params['max_depth']})
        #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado
        # #Código elimninado por ser de uso privado        
        for metrica,valor in params_context.items():
            mlflow.log_metric(metrica, valor)

        mlflow.set_tags({"Tipo_modelo": config['tipo_de_modelo_rec_pers']})
        mlflow.set_tags({"Archivo_tipo": config['tipos_de_archivos_mlflow']['tipo_sklearn']})

        #Nombre modelo 
        mlflow.sklearn.log_model(model,config['nombresDe_modelos_xgboost']+llave,input_example=input_example)

        mlflow.log_metric("precision", metricas[0])
        mlflow.log_metric("recall", metricas[1])


def Entrenar_modelos_por_clase(Diccionario_entrenable,params_context,nuevo_umbral,versionar=True):
    """Entrenamiento y validación de modelos de clasificación por clase"""
    
    Modelos_Entrenados = {}
    Resultados_entrenamiento_test = {}
    Resultados_entrenamiento_train = {}

    for ky, vl in tqdm(Diccionario_entrenable.items(), desc="Entrenando modelos", unit="modelo"):

        Modelos_Entrenados[ky] = trainModel_unitario(vl[0],vl[1]) #inputs: X -> 0 y y -> 1 #outputs: X_train[0],X_test[1],y_train[2],y_test[3],model[4],best_params_[5],columnas[6]
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

        #Métricas en entrenamiento

        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

        Resultados_entrenamiento_test[ky] = {'Metrics':evaluarModelo(y_pred,Modelos_Entrenados[ky][3]),'y_pred':y_pred}

        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado
        #Código elimninado por ser de uso privado

        #Configuración MLFLOW
        if versionar:
            Versionar_MlFlow(model=Modelos_Entrenados[ky])
                
    return {'Models':Modelos_Entrenados,'Metricas_test':Resultados_entrenamiento_test,'Metricas_train':Resultados_entrenamiento_train}

def modelPredict(model,train):
    """ Generación de predicciones para los modelos """    

    ypred = model.predict(train)
    ypred_proba = model.predict_proba(train)
    return ypred,ypred_proba


def evaluarModelo(y_pred,y_true):

    """
    Esta función toma las etiquetas verdaderas y predichas (que pueden estar en formato multilabel) y:
    1. Convierte las etiquetas a un formato plano.
    2. Calcula la matriz de confusión y la visualiza.
    3. Calcula otras métricas de clasificación como precisión, recall, F1-score y accuracy.
    """

    # 1. Accuracy (Precisión global)
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    
    # Usamos 'average=micro' para tener en cuenta todas las clases en multiclase/multilabel
    precision = precision_score(y_true_flat, y_pred_flat)
    recall = recall_score(y_true_flat, y_pred_flat)
    f1 = f1_score(y_true_flat, y_pred_flat)

    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

    # Imprimir las métricas calculadas
    return precision,recall,f1,accuracy,AUC_metric



def Metricas_globales(Resultados_de_modelos):

    """ 
    Para evaluar las métricas globales de los modelos
    """
    
    y_pred_total = np.array([])
    y_test_total = np.array([])

    for ky,valor in Resultados_de_modelos['Metricas_test'].items():
        y_pred_total = np.append(y_pred_total,valor['y_pred'])
        y_test_total = np.append(y_test_total,Resultados_de_modelos['Models'][ky][3].flatten())

    metricas = evaluarModelo(y_pred=y_pred_total,y_true=y_test_total)
    Graficar_AUC(y_test=y_test_total,y_pred=y_pred_total)

    return metricas

def Graficar_AUC(y_test,y_pred):
    """Gráfica el AUC"""
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado
    #Código elimninado por ser de uso privado

