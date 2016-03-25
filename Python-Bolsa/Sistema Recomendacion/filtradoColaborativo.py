import pandas as pd
import numpy as np
from collections import OrderedDict

# 1. OBTENEMOS LOS DATOS
movies_df = pd.read_table('movies.dat', header=None, sep='::', names=['movie_id', 'movie_title', 'movie_genre'])
# we convert the movie genres to a set of dummy variables
movies_df = pd.concat([movies_df, movies_df.movie_genre.str.get_dummies(sep='|')], axis=1)
movie_categories = movies_df.columns[3:]
print (movies_df.head())

ratings_df = pd.read_table('ratings.dat', header=None, sep='::', names=['user_id', 'movie_id', 'rating', 'timestamp'])
#Borramos al fecha en la que el rating fue creado.
del ratings_df['timestamp']
#reemplazamos la id de la película por su titulo para tener una mayor claridad
ratings_df = pd.merge(ratings_df, movies_df, on='movie_id')[['user_id', 'movie_title', 'movie_id','rating']]
print (ratings_df.head())

# Pasamos los datos a filas para usuarios y peliculas para columnas
ratings_mtx_df = ratings_df.pivot_table(values='rating', index='user_id', columns='movie_title')
ratings_mtx_df.fillna(0, inplace=True)
movie_index = ratings_mtx_df.columns
print (ratings_mtx_df.head())

# 2. CALCULAMOS MATRIZ DE CORRELACION
corr_matrix = np.corrcoef(ratings_mtx_df.T)
print (corr_matrix.shape)

# 3. LISTAMOS LAS PELICULAS CON MAYOR CORRELACION
favoured_movie_title = 'Toy Story (1995)'
favoured_movie_index = list(movie_index).index(favoured_movie_title)
P = corr_matrix[favoured_movie_index]

#solo devolvemos las películas con la mayor correlación con Toy Story
print (list(movie_index[(P>0.4) & (P<1.0)]))

# 4. RECOMENDACION DE PELICULAS A UN USUARIO
def get_movie_similarity(movie_title):
    '''Devuelve el vector de correlación para una película'''
    movie_idx = list(movie_index).index(movie_title)
    return corr_matrix[movie_idx]

def get_movie_recommendations(user_movies):
    '''Dado un grupo de películas, devolver las mas similares'''
    movie_similarities = np.zeros(corr_matrix.shape[0])
    for movie_id in user_movies:
        movie_similarities = movie_similarities + get_movie_similarity(movie_id)
    similarities_df = pd.DataFrame({
        'movie_title': movie_index,
        'sum_similarity': movie_similarities
        })
    similarities_df = similarities_df[~(similarities_df.movie_title.isin(user_movies))]
    similarities_df = similarities_df.sort_values(by=['sum_similarity'], ascending=False)
    return similarities_df

sample_user = 21
print (ratings_df[ratings_df.user_id==sample_user].sort_values(by=['rating'], ascending=False))

sample_user_movies = ratings_df[ratings_df.user_id==sample_user].movie_title.tolist()
recommendations = get_movie_recommendations(sample_user_movies)

#Obtenemos las 20 películas con mejor puntuación
print (recommendations.movie_title.head(20))



