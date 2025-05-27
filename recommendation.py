import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the movie dataset
# Make sure 'movies.csv' is in the same folder as this script
movies = pd.read_csv('movies.csv')

# Step 2: Combine 'genre' and 'description' to build a rich content base
movies['content'] = movies['genre'] + ' ' + movies['description']

# Step 3: Convert text content into numerical vectors using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
content_vectors = vectorizer.fit_transform(movies['content'])

# Step 4: Calculate similarity between movies based on their content
similarity_scores_matrix = cosine_similarity(content_vectors, content_vectors)


# Step 5: Function to recommend movies similar to a given title
def recommend_movies(title, sim_matrix=similarity_scores_matrix):
    try:
        # Find the index of the selected movie
        idx = movies.index[movies['title'] == title].tolist()[0]
    except IndexError:
        return ["Sorry, that movie is not in the list."]

    # Get pairwise similarity scores for this movie
    scores = list(enumerate(sim_matrix[idx]))

    # Sort by similarity score, ignoring the movie itself
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:6]]  # Top 5 similar movies

    # Return recommended titles
    return movies['title'].iloc[top_indices].tolist()


# Step 6: Test the recommendation system
user_input = 'The Matrix'
print(f"\nRecommended movies for '{user_input}':")
for movie in recommend_movies(user_input):
    print(f"- {movie}")
