class MusicMatcher:
    def calculate_music_compatibility(self, user1, user2):
        score = 0
        weights = {
            'artists': 0.4,
            'genres': 0.3,
            'tracks': 0.3
        }
        
        # Calculate artist overlap
        common_artists = set(user1.top_artists) & set(user2.top_artists)
        artist_score = len(common_artists) / max(len(user1.top_artists), len(user2.top_artists))
        
        # Similar calculations for genres and tracks
        return (artist_score * weights['artists'] + 
                genre_score * weights['genres'] + 
                track_score * weights['tracks'])