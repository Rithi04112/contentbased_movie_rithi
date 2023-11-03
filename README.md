

# Movie Recommendation System

The Movie Recommendation System is a web application that allows users to receive movie recommendations based on the input of a movie title. The system uses a combination of natural language processing and machine learning techniques to suggest relevant movie choices.

## Features

- **Input Movie Title:** Enter the title of a movie you like.
- **Get Recommendations:** Click the "Recommend" button to receive a list of recommended movies based on your input.

## Frontend

The frontend of the application is built using React. It provides a user-friendly interface for entering a movie title and displays the recommended movies. Here's how it works:

1. Enter the title of a movie you're interested in.
2. Click the "Recommend" button to fetch movie recommendations.

If no recommendations are found or if there's an error, an appropriate message will be displayed.

## Backend

The backend of the application is developed using Flask, a Python web framework. It handles the recommendation logic by processing the input movie title, performing calculations, and returning the recommended movies.

The backend performs the following steps:

1. Loads and preprocesses movie data, including movie titles, overviews, genres, keywords, cast, and crew.
2. Utilizes natural language processing techniques to create a combined set of tags from movie data.
3. Computes similarity between movies based on the tags.
4. Recommends a list of movies that are most similar to the input movie title.

## Usage

1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Start the Flask backend by running `python app.py`. The backend server runs on port 5001.
4. Navigate to the `frontend` directory and run the React frontend by executing `npm install` followed by `npm start`. The frontend runs on the default port 3000.

## Note

- Make sure you have the required dataset files (e.g., `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`) in your specified file path for the backend to function properly.

## Technologies Used

- **Frontend:** React
- **Backend:** Flask
- **Machine Learning:** CountVectorizer and Cosine Similarity
- **Data Preprocessing:** Pandas and NLTK (Natural Language Toolkit)

---

This README file provides an overview of the Movie Recommendation System, its features, usage instructions, and the technologies used in both the frontend and backend. It's recommended to include any additional details, setup instructions, or deployment information specific to your environment.

![image](https://github.com/Rithi04112/contentbased_movie_rithi/assets/98526095/431f0886-9999-4e59-9a7e-74a5cd1b1748)

![image](https://github.com/Rithi04112/contentbased_movie_rithi/assets/98526095/9ea1126a-fa12-446f-bb2e-fc86c428775b)
