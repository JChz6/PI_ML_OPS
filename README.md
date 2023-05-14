# Proyecto Individual N°1: PI_ML_OPS


💡 Contexto:
Soy un data scientist desarrollando un proyecto para una start-up proveedora de servicios de agregación de plataformas de streaming. Este proyecto consta de crear el modelo de Machine Learning para un sistema de recomendación de películas.

El proyecto comienza con la recepción de los datos, los cuales requieren un AMPLIO trabajo de limpieza, transformación y desanidamiento.

Empecemos:

Guía de navegación de archivos:
 
 - README - (Usted está aquí) Guía de navegación e instrucciones
 - main.py - Archivo python que contiene las funciones que consume la API.
 - ETL.ipynb - Proceso de transformación, y limpieza de los datos.
 - Carpeta pycache - carpeta necesaria para el funcionamiento de la API.
 - movies_dataset.csv - Archivo original con los datos sin procesar
 - movies_limpio.csv - Archivo resultante del proceso de ETL, con los datos listos para su consumo.
 - requirements.txt - Librerías necesarias para el funcionamiento de la API.
 - CARPETA Codigo ML - Archivos con los que trabaja el modelo de ML para el sistema de recomendación:
 - EDA.ipynb - Análisis exploratorio de los datos y primera demo del sistema de recomendación.
 - movies_ML_training.csv - Archivo que consumirá la API para las consultas al sistema de recomendación (creado en EDA.ipynb)
 - ETL_ML.ipynb - Proceso de transformación, y limpieza de los datos (específicamente para elaborar el modelo de ML)
 - movies_ML.csv - Archivo resultante del proceso elaborado en ETL_ML.ipynb
 

main.py   ---- FUNCIONES:

1. peliculas_mes(mes): Se ingresa el mes y la función retorna la cantidad de películas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero')

2. peliculas_dia(dia): Se ingresa el día y la función retorna la cantidad de películas que se estrenaron ese dia de la semana (en str, ejemplo 'lunes') historicamente

3. franquicia(franquicia): Se ingresa la franquicia, retornando la cantidad de películas, ganancia total y promedio

4. peliculas_pais(pais): Ingresas el país, retornando la cantidad de películas producidas en el mismo

5. productoras(productora): Ingresas la productora, retornando la ganancia total y la cantidad de películas que produjeron

6. retorno(pelicula): Ingresas la pelicula, retornando la inversión, la ganancia, el retorno y el año en el que se lanzó

7. recomendacion('titulo'): Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores



  ***** Consulta las funciones en ESTE LINK *****  https://pi-ml-ops-jchavez.onrender.com/docs
  
  
  
Herramientas y librerías utilizadas:
- Python
- Pandas
- Numpy
- Scikit-learn
- FastAPI
- Uvicorn
- Render
