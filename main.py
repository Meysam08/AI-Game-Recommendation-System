# v1.py
# Simple Genre-based Game Recommendation System

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample mini dataset
games = [
    {"title": "The Witcher 3", "genre": "RPG Fantasy Open-World"},
    {"title": "Cyberpunk 2077", "genre": "RPG Sci-Fi Open-World"},
    {"title": "DOTA 2", "genre": "MOBA Multiplayer Competitive"},
    {"title": "League of Legends", "genre": "MOBA Multiplayer PvP"},
    {"title": "GTA V", "genre": "Action Open-World Crime"},
    {"title": "Skyrim", "genre": "RPG Fantasy Open-World"}
]

# Extract genres
corpus = [g["genre"] for g in games]

# Convert genres to vector
vectorizer = TfidfVectorizer()
genre_vectors = vectorizer.fit_transform(corpus)

def recommend_by_genre(genre_query, top_k=3):
    query_vec = vectorizer.transform([genre_query])
    similarity = cosine_similarity(query_vec, genre_vectors).flatten()

    top_indices = similarity.argsort()[::-1][:top_k]

    return [games[i]["title"] for i in top_indices]


if __name__ == "__main__":
    print("=== Game Recommendation System v1 ===")
    user_genre = input("Enter a genre: ")
    recs = recommend_by_genre(user_genre)
    print("\nRecommended games:")
    for r in recs:
        print("-", r)
