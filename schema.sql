-- Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    spotify_id VARCHAR(100),
    age INT,
    location POINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Music Preferences Table
CREATE TABLE music_preferences (
    user_id INT REFERENCES users(user_id),
    artist_id VARCHAR(100),
    genre VARCHAR(50),
    weight FLOAT
);

-- Matches Table
CREATE TABLE matches (
    match_id SERIAL PRIMARY KEY,
    user1_id INT REFERENCES users(user_id),
    user2_id INT REFERENCES users(user_id),
    compatibility_score FLOAT,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);