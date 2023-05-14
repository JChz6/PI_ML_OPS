from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('movies_limpio.csv')
df = pd.read_csv('Codigo ML/movies_ML_training.csv') #Este dataset servirá como entramiento del modelo

#Machine Learning
#Creo la matriz de características
tfidf = TfidfVectorizer(stop_words='english')
overview_matrix = tfidf.fit_transform(df['text'])

app = FastAPI()

#http://127.0.0.1:8000

@app.get("/")
async def saludar():
    return  "Hola Mundo"



#************************ FUNCIÓN 1 ************************

@app.get("/peliculas_mes/{mes}")
async def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''

    movies['release_date'] = pd.to_datetime(movies['release_date'])

    if mes.title() == 'Enero':
        mesnum = 1
    elif mes.title() == 'Febrero':
        mesnum = 2
    elif mes.title() == 'Marzo':
        mesnum = 3
    elif mes.title() == 'Abril':
        mesnum = 4
    elif mes.title() == 'Mayo':
        mesnum = 5
    elif mes.title() == 'Junio':
        mesnum = 6
    elif mes.title() == 'Julio':
        mesnum = 7
    elif mes.title() == 'Agosto':
        mesnum = 8
    elif mes.title() == 'Septiembre':
        mesnum = 9
    elif mes.title() == 'Setiembre':
        mesnum = 9
    elif mes.title() == 'Octubre':
        mesnum = 10
    elif mes.title() == 'Noviembre':
        mesnum = 11
    elif mes.title() == 'Diciembre':
        mesnum = 12
    else:
        return {'ERROR':'Inserta un nombre de mes válido'}

    respuesta = len(movies[movies['release_date'].dt.month == mesnum])
    return {'mes':mes, 'cantidad': respuesta}


#************************ FUNCIÓN 2  ************************

@app.get("/peliculas_dia/{dia}")
async def peliculas_dia(dia:str):

    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia historicamente'''
    
    dias = {0:'lunes',
        1: 'martes',
        2: 'miercoles',
        3: 'jueves',
        4: 'viernes',
        5: 'sabado',
        6: 'domingo'}
    
    movies['release_date'] = pd.to_datetime(movies['release_date'])

    for key,value in dias.items():
        if dia == value:
            dianum = key
            respuesta = len(movies[movies['release_date'].dt.weekday == dianum])
            return {'dia':dia, 'cantidad':respuesta}
    return {'ERROR': 'coloca un día válido'}


#************************ FUNCIÓN 3 ************************

@app.get("/franquicia/{franquicia}")
async def franquicia(franquicia:str):

    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''

    df_franquicia = movies[movies['belongs_to_collection'] == franquicia]
    cantidad = len(df_franquicia)
    ganancia_total = df_franquicia['revenue'].sum()
    ganancia_promedio = df_franquicia['revenue'].mean()    
    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}



#************************ FUNCIÓN 4 ************************

@app.get("/peliculas_pais/{pais}")
async def peliculas_pais(pais:str):
    
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''

    respuesta = len(movies[movies['production_countries'].str.contains(pais, na=False)])
    
    return {'pais':pais, 'cantidad':respuesta}



#************************ FUNCIÓN 5  ************************

@app.get("/productoras/{productora}")
async def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'''
    df_productora = movies[movies['production_companies'].str.contains(productora, na=False)]
    ganancia_total = df_productora['revenue'].sum()
    cantidad = len(df_productora)
    return {'productora':productora, 'ganancia_total':ganancia_total, 'cantidad':cantidad}


#************************ FUNCIÓN 6 ************************

@app.get("/retorno/{pelicula}")
async def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    if pelicula not in movies['title'].values:
        return {'ERROR': 'Esa película no existe'}
    titulo = movies[movies['title'] == pelicula][0:1]
    inversion = float(titulo['budget'].values)
    ganancia = float(titulo['revenue'].values)
    retorno = float(titulo['return'].values)
    anio = int(titulo['release_year'].values)

    return {'pelicula':pelicula, 'inversion':inversion, 'ganancia':ganancia,'retorno':retorno, 'anio':anio}



#************************ ML ************************

# función de recomendación basada en los datos concatenados en "text"
@app.get("/recomendacion/{titulo}")
def recomendacion(titulo):
    idx = df[df['title']==titulo].index[0]
    sim_scores = cosine_similarity(overview_matrix[idx], overview_matrix)
    sim_scores = list(enumerate(sim_scores[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    respuesta = pd.DataFrame(df.iloc[movie_indices]['title'])
    respuesta = list(respuesta['title'].values)
    return {'lista recomendada': respuesta}