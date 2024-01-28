# Microsoft Engage 2022 Project - Movie Recommender System

## Overview

Welcome to the Movie Recommender System, a project developed as part of Microsoft Engage 2022. This system leverages the power of Streamlit to provide users with personalized movie recommendations based on a trained dataset. The dataset used is the TMDB5000 dataset from Kaggle, and the recommendation model is built using collaborative filtering.

## Features

- **Interactive Interface**: User-friendly Streamlit interface for selecting movies and obtaining recommendations.
- **Movie Information**: Displays selected movie details, including title and poster.
- **Top 5 Recommendations**: Recommends the top 5 movies similar to the selected one, along with their posters.

## How to Use

1. Ensure you have Python installed on your machine.
2. Install the required libraries by running: `pip install streamlit pandas requests`.
3. Clone the repository to your local machine.
4. Run the Streamlit app using the command: `streamlit run main.py`.
5. Select a movie from the dropdown menu and click the "Recommend" button.
6. Explore the top 5 recommended movies along with their posters.

## Code Structure

- `main.py`: Streamlit app script.
- `movies.pkl`: Pickled file containing trained movie recommender system.
- `similar.pkl`: Pickled file containing similarity scores between movies.

## API Integration

The project integrates with The Movie Database (TMDb) API to fetch movie posters based on movie IDs.

## Acknowledgments

- **Dataset**: TMDB5000 dataset from Kaggle.
- **API**: [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)


Feel free to contribute, report issues, or suggest improvements. Happy movie watching! 🎬🍿
