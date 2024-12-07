# Predicción de Siguiente Compra en Retail
#### Este es un copia de mi proyecto oficial de predicción de próximas compras de clientes. El código ha sido simplificado y se han eliminado las credenciales para dar una idea de la estructura del proyecto sin comprometer la privacidad o seguridad de la información.
El objetivo de este repositorio es dar una idea de la posibilidad y potencia del proyecto de recomendación personalizada a clientes.


Este proyecto busca optimizar la personalización de recomnedaciones en retail mediante la predicción de los próximos productos que un cliente puede adquirir, basándose en su historial de compras y patrones de consumo de otros usuarios. El sistema ofrece recomendaciones personalizadas, generalizadas y de recompra para clientes conocidos, y también proporciona recomendaciones iniciales para clientes nuevos.

![image](https://github.com/user-attachments/assets/0d418e90-3fa2-48c5-b55c-026adc07f2f7)

## Descripción del Proyecto

El sistema implementa cuatro enfoques de recomendación:

### I.
1. *Modelo de Recomendación Personalizada (XGBoost)*
2. *Modelo de Recomendación Generalizada (Apriori)*

### II.

1. *Modelo de recom prods restringido*


## Tecnologías

Este proyecto emplea las siguientes tecnologías y frameworks:

- *Python* para el desarrollo de modelos y funciones.
- *MLflow* para el versionado y registro de modelos.
- *Oracle* Para la conexión a las bases de datos

## Estructura del Proyecto
```bash
├── data/                    # Almacenamiento de datasets
│   ├── Pcks_models.py       # Modelos entrenados y gestionados en MLflow
│   ├── stop_baskets/        # Almacenamiento de reglas de negocios
├── models/                  # Modelos entrenados y gestionados en MLflow
│   ├── Model_Xgboost/       # Entrenamiento,medición e inferencia de Xgboost
│   ├── Model_Apriori/       # Entrenamiento,medición e inferencia de Apriori
│   ├── src_recProduct/      # Cálculo de productos más probables
├── mains/                   # Código fuente
│   ├── ARECGER.py           # Código pipeline, entrenamiento y predict Apriori
│   ├── XRECPER.py           # Código pipeline, entrenamiento y predict Xgboost
│   ├── InferClient.py       # Realizar inferencia a un cliente
├── sdk/                     # Kit de código
├── transforms/              # Transformaciones para modelos
├── README.md                # Descripción del proyecto
└── requirements.txt         # Dependencias del proyecto
├── Api.py                   # Generación de api modelo
├── main.py                  # Predicción y actualización semanal 
```

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/EsteRepo.git
   cd EsteRepo

   pip install -r requirements.txt
   ```

## Uso
### Entrenamiento de Modelos:

- Ejecuta main.py 

## Predicciones:

- Usa el script main.py con las funciones de cada modelo para realizar predicciones y recomendaciones de los clientes que han comprado en los últimos 8 días.
- Usa el script InferClient.py con con la variable cliente insertando un número de Identificación para generar la respuesta en formato Json.

## Registro y Versionado
- Los modelos están gestionados y versionados en MLflow, permitiendo realizar un seguimiento de los cambios, los parámetros utilizados y los resultados de cada iteración.
