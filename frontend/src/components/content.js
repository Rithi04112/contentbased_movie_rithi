import React, { useState } from 'react';
import './Content.css';

const Content = () => {
  const [movie, setMovieInput] = useState('');
  const [recommendedMovies, setRecommendedMovies] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');

  const handleMovieChange = (event) => {
    setMovieInput(event.target.value);
  };

  const handleApiError = (error) => {
    console.error(error);
    setRecommendedMovies([]);
    setErrorMessage('Error fetching recommendations.');
  };

  const handleRecommendation = () => {
    fetch(`http://127.0.0.1:5001/recommend?movie=${movie}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.recommendations && data.recommendations.length > 0) {
          setRecommendedMovies(data.recommendations);
          setErrorMessage('');
        } else {
          setRecommendedMovies([]);
          setErrorMessage('No recommendations found.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        setErrorMessage('No data found for the given input.');
      });
  };

  return (
    <div className="container">
      <h1>Movie Recommendation System</h1>
      <div className="search-container">
        <input
          type="text"
          placeholder="Search for a movie..."
          value={movie}
          onChange={handleMovieChange}
        />
        <button onClick={handleRecommendation}>Recommend</button>
      </div>
      <div className="recommendations">
        <h2>Recommended Movies:</h2>
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        <div className="movie-cards">
          {recommendedMovies.map((movie, index) => (
            <div className="movie-card" key={index}>
              <h3>{movie.title}</h3>
              <p>Overview: {movie.overview}</p>
              <p>Cast: {movie.cast.join(', ')}</p>
              <p>Genres: {movie.genres.join(', ')}</p>
             
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Content;

