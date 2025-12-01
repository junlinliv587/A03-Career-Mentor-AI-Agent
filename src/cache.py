import hashlib
import pickle
import os
from datetime import datetime, timedelta

class ResponseCache:
    def __init__(self, cache_dir="./cache", ttl_hours=24):
        self.cache_dir = cache_dir
        self.ttl = timedelta(hours=ttl_hours)
        os.makedirs(cache_dir, exist_ok=True)
    
    def _get_cache_key(self, user_profile):
        """Generate unique cache key from user profile"""
        profile_str = f"{user_profile['current_level']}_{user_profile['career_goal']}_{user_profile['hours_per_week']}_{user_profile['timeline_months']}"
        return hashlib.md5(profile_str.encode()).hexdigest()
    
    def get(self, user_profile):
        key = self._get_cache_key(user_profile)
        cache_file = os.path.join(self.cache_dir, f"{key}.pkl")
        
        if os.path.exists(cache_file):
            # Check if cache is expired
            if datetime.now() - datetime.fromtimestamp(os.path.getmtime(cache_file)) < self.ttl:
                with open(cache_file, 'rb') as f:
                    return pickle.load(f)
        return None
    
    def set(self, user_profile, response):
        key = self._get_cache_key(user_profile)
        cache_file = os.path.join(self.cache_dir, f"{key}.pkl")
        
        with open(cache_file, 'wb') as f:
            pickle.dump(response, f)