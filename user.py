class UserProfile:
    def __init__(self):
        self.user_id = None
        self.name = None
        self.age = None
        self.location = None
        self.spotify_token = None
        self.music_preferences = {
            'favorite_genres': [],
            'favorite_artists': [],
            'recently_played': [],
            'top_tracks': []
        }
        self.matching_preferences = {
            'age_range': (18, 99),
            'distance': 50,  # km
            'gender_preference': None
        }