import pandas as pd
import ast
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This line enables CORS for your Flask app


# Load and preprocess the movie data
# Load and preprocess the movie data
movies = pd.read_csv(r'C:\B RITHIKAA\movie_recommendation_system\tmdb_5000_movies.csv', low_memory=False)
credits = pd.read_csv(r'C:\B RITHIKAA\movie_recommendation_system\tmdb_5000_credits.csv', low_memory=False)


movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

def convert(text):
    l = []
    for i in ast.literal_eval(text):
        l.append(i['name'])
    return l

movies['genres'] = movies['genres'].apply(convert)

def convert_cast(text):
    l = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            l.append(i['name'])
        counter += 1
    return l

movies['cast'] = movies['cast'].apply(convert_cast)

def fetch_director(text):
    l = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            l.append(i['name'])
            break
    return l

movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

def remove_space(word):
    l = []
    for i in word:
        l.append(i.replace(" ", ""))
    return l

movies['cast'] = movies['cast'].apply(remove_space)
movies['crew'] = movies['crew'].apply(remove_space)
movies['genres'] = movies['genres'].apply(remove_space)
movies['keywords'] = movies['keywords'].apply(remove_space)


# Modify the line where you concatenate columns
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']  


# The rest of the code remains the same

new_df = movies[['movie_id', 'title', 'tags']]
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: " ".join(x))


# Set up CountVectorizer and Cosine Similarity
cv = CountVectorizer(max_features=5000, stop_words="english")
vector = cv.fit_transform(new_df['tags']).toarray()
similarity = cosine_similarity(vector)

# Set up the stemmer
ps = PorterStemmer()
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x: " ".join([ps.stem(word) for word in x.split()]))


def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)

    recommended_movies = []
    for i in distances[1:8]:
        movie_info = {
            'title': new_df.iloc[i[0]].title,
           
            'overview': ' '.join(movies['overview'].iloc[i[0]]),
            'cast': movies['cast'].iloc[i[0]],
            'genres': movies['genres'].iloc[i[0]],
        }
        recommended_movies.append(movie_info)

    return recommended_movies

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    if request.method == 'GET':
        movie = request.args.get('movie')
        recommended_movies = recommend(movie)
        return jsonify({'recommendations': recommended_movies})

if __name__ == '__main__':
    app.run(debug=True, port=5001)








