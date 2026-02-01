import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
def recommend(movie_title, n=5):
    if movie_title not in movie_user_matrix_filled.index:
        print("Movie not found")
        return
    idx = movie_user_matrix_filled.index.get_loc(movie_title)

    similarity_scores = list(enumerate(similarity_matrix[idx]))
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended movies:")
    for i in similarity_scores[1:n+1]:
        print(movie_indices[i[0]])


if __name__=="__main__":
    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")

    movie_data = pd.merge(ratings, movies, on="movieId")

    movie_user_matrix = movie_data.pivot_table(
        index="title",
        columns="userId",
        values="rating"
    )

    movie_user_matrix_filled = movie_user_matrix.fillna(0)

    similarity_matrix = cosine_similarity(movie_user_matrix_filled)

    # Create movie index mapping
    movie_indices = pd.Series(
        movie_user_matrix_filled.index,
        index=range(len(movie_user_matrix_filled))
    )
    recommend(input(),input())

