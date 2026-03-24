import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Create a simple dataset of movies
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Dark Knight', 'Inception', 'Toy Story', 'The Avengers', 'Cars'],
    'genres': ['Action Crime Drama', 'Action Sci-Fi', 'Animation Adventure Comedy', 'Action Sci-Fi', 'Animation Adventure Comedy']
}

df = pd.DataFrame(data)

def get_recommendations(movie_title, df):
    # 2. Vectorize the genres (convert text to numbers)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['genres'])

    # 3. Compute Cosine Similarity (how similar are the genre vectors?)
    cosine_sim = cosine_similarity(count_matrix)

    # 4. Get the index of the movie that matches the title
    try:
        idx = df[df['title'] == movie_title].index[0]
    except IndexError:
        return "Movie not found in database."

    # 5. Get pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 6. Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 7. Get the scores of the most similar movies (excluding itself)
    sim_scores = sim_scores[1:3]

    # 8. Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 2 most similar movies
    return df['title'].iloc[movie_indices].tolist()

# --- Testing the System ---
target_movie = "Inception"
recommendations = get_recommendations(target_movie, df)

print(f"If you liked '{target_movie}', you might also like:")
for movie in recommendations:
    print(f"- {movie}")