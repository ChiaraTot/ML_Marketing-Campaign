## 🎯  Segmentación de Clientes con Machine Learning para Campañas de Marketing 

### 📌 Descripción del Proyecto 

Este proyecto implementa técnicas avanzadas de Machine Learning para analizar y segmentar clientes, con el objetivo de optimizar estrategias de marketing mediante la identificación de grupos homogéneos con características similares.

### 🚀 Características Principales

- Técnica de Segmentación: Clustering con K-Means
- Objetivo: Personalización de estrategias de marketing
- Enfoque: Análisis cuantitativo basado en datos numéricos

#### 📊 Fuente de Datos

Dataset: Conjunto de datos opensource disponible en Kaggle


### 💡 Importancia de la Segmentación en Marketing
La segmentación de clientes en Marketing es fundamental para:

✅ Diseñar campañas más efectivas y personalizadas  
✅ Optimizar la asignación de recursos de marketing  
✅ Aumentar la retención y fidelización de clientes  
✅ Maximizar el retorno de inversión (ROI) en estrategias publicitarias.


#### 🔍 Tipos de Segmentación Explorados

En funcion del las variables proporcionadas en el dataset, se ha podido efectuar segmentacion enfocandose en carateristicas:

``📊 Demográficas`` : Edad, Ingresos, Composición familiar, Nivel educativo  
``📈 Conductuales`` : Hábitos de compra, Frecuencia de compras, Canales preferidos


#### 🛠 Estructura del Repositorio

``src/data_sample`` # Archivo con los datos
project-root/
│
├── src/
│   ├── data_sample/          # Archivo con los datos
│   ├── img/                  # Imágenes del proyecto
│   ├── notebooks/            # Cuadernos de experimentación
│   ├── results_notebook/     # Notebook final del proyecto
│   ├── models/               # Modelos de Machine Learning guardados
│   └── utils/                # Módulos y funciones auxiliares
│
├── PRESENTACION.ppt          # Presentacion del proyecto
└── README.md                 # Documentación del proyecto

Ruta repositorio : git clone https://github.com/ChiaraTot/ML_Marketing-Campaign

 ### 🧠Metodología de Machine Learning
 #### Algoritmo Principal: K-Means

##### Tipo: Aprendizaje no supervisado
##### Objetivo: Agrupar clientes en clusters basados en similitudes
##### Proceso:
   ``1.Preparación y limpieza de datos``
   2.Elaboración EDA
   3.Selección de características relevantes
   4.Aplicación del algoritmo K-Means
   5.Análisis de resultados y visualización de clusters



#### 🔬 Tecnologías Utilizadas

- Python 3.12.7
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn


####📈Métricas de Evaluación

- Coeficiente de Silhouette
- Inercia (Within-Cluster Sum of Squares) :Metodo del codo
- Distribución de clusters : Visualizacion 'cuchillos'

### 🎯 Clustering Profiling

Interpretacion de los resultados y propuestas estrategias de Marketing por cada Cluster.

### 📞 Contacto
www.linkedin.com/in/ctotaro



----------------------------------------------------

# ML_Marketing-Campaign
Repositorio que recoge el proyecto de ML que trata de hacer predicciones sobre Campañas de Marketing - predicciones de respuesta y optimización de segmentación de perfiles -

📌 Proyecto: Segmentación de clientes con machine learning
📊 Marketing e Inteligencia Artificial

🎯 Objetivo de la práctica
En este proyecto, se explora un dataset de campañas de marketing y se aplica segmentación de clientes utilizando técnicas de Machine Learning (Clustering).
El propósito es identificar grupos de clientes con características similares para que se puedan diseñar estrategias de marketing personalizadas para cada segmento.

Fuente de datos: 
Se ha empleado el dataset opensource disponible en kaggle: 

💡 ¿Por qué es importante la segmentación en marketing?¶
La segmentación de clientes es una estrategia clave en marketing que permite dividir a los clientes en grupos homogéneos en función de ciertas características. Esto ayuda a:

✅ Diseñar campañas más efectivas y personalizadas.
✅ Mejorar la asignación de recursos en marketing.
✅ Aumentar la retención y fidelización de clientes.
✅ Maximizar el retorno de inversión (ROI) en estrategias publicitarias.

Existen varios enfoques para segmentar clientes, como:

Demográficos: Edad, ingresos, estado civil, educación.
Conductuales: Hábitos de compra, frecuencia de compras, canales preferidos.
Psicográficos: Intereses, valores, estilo de vida.
Geográficos: Ubicación, región, clima.

🔬 Segmentación y modelos de decisión en marketing
Se ha utilizado un modelo cuantitativo, es decir se apoya en datos numéricos y métricas para realizar análisis de segmentación y clasificación

📌 En este caso, se a utilizaso el algoritmo de Machine Learning K-Means, un algoritmo de aprendizaje no supervisado que agrupa clientes en clusters basándose en sus similitudes.

Describir la estructura de directorios del repositorio: 
el codigo sigue la siguiente estructura de carpetas:
1. ``src/data_sample``: los archivos de datos de muestra utilizados en el proyecto que permitan ejecutar el código. [Recuerda no subir a GitHub archivos demasiado pesados]
2. ``src/img``: Imágenes que hayas necesitado para tu proyecto. 
3. ``src/notebooks``: los notebooks usados para pruebas.
4. ``src/results_notebook``: el notebook final resultante del proyecto.
5. ``src/models``: los modelos guardados al ejecutar el código del proyecto.
6. ``src/utils``: todos los modulos, funciones auxiliares o clases creadas para el desarrollo del proyecto.