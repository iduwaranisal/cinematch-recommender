# 🍿 CineMatch - Movie Recommender System

CineMatch is a Content-Based Movie Recommender System that suggests movies based on user preferences. By analyzing movie tags (genres, cast, crew, and keywords), it finds and recommends the top 5 most similar movies to your selection, complete with their official posters.

## 💡 About The Project

Finding a good movie to watch can be overwhelming. CineMatch simplifies this by using a machine learning algorithm (Cosine Similarity) to recommend movies that share similar attributes with the ones you already love. 

Due to GitHub's file size limits, the large machine learning similarity matrix (`similarity.pkl`) is securely hosted on Google Drive and is dynamically downloaded when the app runs for the first time using `gdown`.

### ✨ Features
* **Accurate Recommendations:** Uses Cosine Similarity to find the best matches.
* **Dynamic Posters:** Fetches high-quality movie posters in real-time via the TMDB API.
* **Smart Downloading:** Automatically handles large ML model files via Google Drive integration.
* **Sleek UI:** Clean and responsive user interface built with Streamlit.

## 🛠️ Built With
* [Python](https://www.python.org/) - Core programming language
* [Streamlit](https://streamlit.io/) - Web framework for the UI
* [Pandas](https://pandas.pydata.org/) - Data manipulation
* [Scikit-Learn](https://scikit-learn.org/) - Machine learning (Cosine Similarity & CountVectorizer)
* [TMDB API](https://www.themoviedb.org/documentation/api) - Fetching movie posters
* [gdown](https://github.com/wkentaro/gdown) - Downloading large files from Google Drive

## 🚀 How to Run Locally

To get a local copy up and running, follow these simple steps.

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR-USERNAME/cinematch-recommender.git](https://github.com/iduwaranisal/cinematch-recommender.git)
cd cinematch-recommender



👨‍💻 Author
Iduwara Nisal Palihawadana * GitHub: @iduwaranisal

⭐️ If you like this project, please give it a star on GitHub!