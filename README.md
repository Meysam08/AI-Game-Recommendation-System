# AI Game Recommendation System

A simple yet effective game recommendation engine that suggests titles based on genre descriptions using **TF-IDF vectorization** and **cosine similarity**.  
Perfect for learning content‑based filtering and text vectorization concepts.

## 🚀 Features

- Takes a genre query (e.g., `"RPG Fantasy Open-World"`) as input.
- Compares the query against a mini dataset of games using TF‑IDF vectors.
- Returns the top‑k most similar games based on genre similarity.
- Lightweight, dependency‑friendly, and easy to extend.

## 🧠 How It Works

1. A small dataset of games with `title` and `genre` fields is defined.
2. The genre strings are vectorized using `TfidfVectorizer` from scikit‑learn.
3. When a user enters a genre query, it is vectorized the same way.
4. Cosine similarity is computed between the query vector and all game genre vectors.
5. The games with the highest similarity scores are recommended.

## 📁 Project Structure

```
AI-Game-Recommendation-System/
├── main.py          # Main recommendation script
└── README.md        
```

## 🛠️ Requirements

- Python 3.7+
- scikit‑learn

Install the required package with:

```bash
pip install scikit-learn
```

## ▶️ How to Run

```bash
python main.py
```

Then enter a genre when prompted. Example:

```
=== Game Recommendation System v1 ===
Enter a genre: RPG Fantasy Open-World

Recommended games:
- The Witcher 3
- Skyrim
- Cyberpunk 2077
```

## 📊 Sample Dataset

| Title            | Genre                               |
|------------------|-------------------------------------|
| The Witcher 3    | RPG Fantasy Open-World              |
| Cyberpunk 2077   | RPG Sci-Fi Open-World               |
| DOTA 2           | MOBA Multiplayer Competitive        |
| League of Legends| MOBA Multiplayer PvP                |
| GTA V            | Action Open-World Crime             |
| Skyrim           | RPG Fantasy Open-World              |

## 🔮 Possible Improvements

- Replace the hardcoded dataset with a real database or CSV/JSON file.
- Add more game attributes (e.g., platform, year, user ratings) for hybrid recommendations.
- Build a web interface using Flask or Streamlit.
- Use a larger game dataset (e.g., from Steam or IGDB).
- Implement collaborative filtering for personalised recommendations.

## 📝 License

This project is open‑source and available under the [MIT License](LICENSE).

## 👤 Author

**Meysam08**  
GitHub: [Meysam08](https://github.com/Meysam08)

---

⭐ Feel free to fork, improve, and use it as a starting point for your own recommendation system projects!
