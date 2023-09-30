# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity

# Conjunto de datos ampliado con más películas y descripciones
data = {
    'movie': [
        'El Rescate del Rey', 'Amor en París', 'Guerreros del Desierto', 'Risas en Nueva York',
        'Misterio en Londres', 'La Venganza del Samurai', 'Bailando bajo la lluvia', 'El Tesoro Perdido'
    ],
    'description': [
        'accion aventura rey rescate', 'romance comedia paris amor', 'accion drama desierto guerra',
        'comedia drama nueva york risas', 'thriller misterio londres detective', 'accion samurai venganza',
        'romance musical lluvia baile', 'aventura tesoro mapa'
    ]
}

# Convertir el diccionario de datos en un DataFrame de pandas
df = pd.DataFrame(data)

# Preparar los datos para Doc2Vec
documents = [TaggedDocument(doc.split(), [i]) for i, doc in enumerate(df['description'])]
model = Doc2Vec(documents, vector_size=5, window=1, min_count=1, workers=4)
embeddings = [model.infer_vector(doc.split()) for doc in df['description']]
cosine_sim_content = cosine_similarity(embeddings, embeddings)

# Conjunto de datos ampliado de calificaciones de usuarios para diferentes películas
ratings = np.array([
    [5, 3, 0, 1, 0, 0, 0, 0],
    [4, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 5, 0, 0, 0, 0],
    [1, 0, 0, 4, 0, 0, 0, 0],
    [0, 1, 5, 4, 0, 0, 0, 0],
    [3, 0, 4, 0, 0, 5, 0, 2]
])

# Factorización de matrices usando SVD
U, sigma, Vt = np.linalg.svd(ratings)
k = 2
U = U[:, :k]
sigma = np.diag(sigma[:k])
Vt = Vt[:k, :]
predicted_ratings = np.dot(np.dot(U, sigma), Vt)

# Cambiar la matriz de calificaciones a un DataFrame con nombres de usuarios y películas
users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
ratings_df = pd.DataFrame(ratings, index=users, columns=data['movie'])

def rate_movie(user, movie, rating):
    """Permite a un usuario calificar una película."""
    if movie in ratings_df.columns and user in ratings_df.index:
        ratings_df.loc[user, movie] = rating
    else:
        print("Usuario o película no encontrados.")

def get_recommendations(user):
    """Obtiene recomendaciones para un usuario."""
    user_index = users.index(user)
    return hybrid_recommendations(user_index)

# Función de recomendaciones híbridas 
def hybrid_recommendations(user_index):
    not_rated = np.where(ratings[user_index] == 0)[0]
    collab_predictions = predicted_ratings[user_index, not_rated]
    rated_by_user = np.where(ratings[user_index] > 0)[0]
    avg_sim_content = cosine_sim_content[rated_by_user, :].mean(axis=0)
    content_predictions = avg_sim_content[not_rated]
    combined_predictions = 0.5 * collab_predictions + 0.5 * content_predictions
    recommended = not_rated[np.argsort(-combined_predictions)]
    return df['movie'].iloc[recommended]

# Ejemplo de uso:
rate_movie('Alice', 'El Rescate del Rey', 5)
print(get_recommendations('Alice'))
