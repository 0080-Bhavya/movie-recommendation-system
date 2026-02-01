# Movie Recommendation System

## Overview
This project implements a movie recommendation system using collaborative filtering and cosine similarity. Movies are recommended based on similarity in user rating patterns.

## Dataset
MovieLens latest small dataset containing 100K+ ratings from 600+ users across 9000+ movies.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn

## Methodology
1. Load movie and ratings datasets.
2. Merge movie titles with ratings.
3. Create movie-user rating matrix.
4. Fill missing ratings with zeros.
5. Compute cosine similarity between movies.
6. Recommend movies based on similarity scores.

## How to Run

1. Clone the repository:
   git clone https://github.com/<your-username>/movie-recommendation-system.git

2. Move into project folder:
   cd movie-recommendation-system

3. Install dependencies:
   python -m pip install -r requirements.txt

4. Run the recommendation script:
   python src/recommendation.py

## Future Improvements
- Personalized user recommendations
- Web interface
- Hybrid recommendation models

