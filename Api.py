from mains import InferClient
from fastapi import FastAPI, Query
import yaml,joblib

with open('configPasillo.yml', 'r',encoding='utf-8') as file:
    config_data = yaml.safe_load(file)


app = FastAPI(title=config_data['title_app'],
    description="Esta API proporciona recomendaciones personalizadas basadas en el historial de compras del cliente.",
    version=config_data['version'],
    contact={
        "name": "Christian Saker",
        "Cell": "+57 300812098",
        "email": "csaker95@gmail.com"
    }
)

#http://127.0.0.1:8000/?cliente=1140880308

@app.get("/")
def Api_Recomendar(
    cliente: str = Query(..., description="Identificador único del cliente"),
    df=None,
    envPasillo: str = config_data['app_uvicor_env'],
    MostrarAntesEliminar: int = None,
    maximo_compras: int = 9999,
    maximo_dias: int = 9999999,
    update_models: bool = False,
    verbose: bool = False,
    tiempos: bool = False,
    update_prods: bool = False):
    """
    Genera recomendaciones personalizadas para un cliente específico utilizando diferentes modelos de predicción.
    """
    # Ejemplo de carga del dataframe para prueba
    if envPasillo == 'dev':
        df = joblib.load('Others/pkl/data_desde_2023.pkl')
        df = df.reset_index()

    with open('configPasillo.yml', 'r',encoding='utf-8') as file:
        config_data = yaml.safe_load(file)

    return InferClient.RealizarRecomendacionesCliente(cliente=cliente,config_data=config_data,df=df,envPasillo=envPasillo,
                                                      MostrarAntesEliminar=MostrarAntesEliminar,maximo_compras=maximo_compras,maximo_dias=maximo_dias,
                                                      update_models=update_models,verbose=verbose,tiempos=tiempos,update_prods=update_prods)