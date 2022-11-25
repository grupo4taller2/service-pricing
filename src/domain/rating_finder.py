import requests
from src.conf.config import Settings
from src.domain.errors import RatingsServiceUnavailableError


class RatingsFinder:
    URL = Settings().RATINGS_SERVICE_REMOTE_URL

    def find_driver_rating(self, driver_username: str):
        full_url = self.URL + f'/drivers/{driver_username}/qualy/average'
        response = requests.get((full_url))
        if response.status_code != 200:
            raise RatingsServiceUnavailableError
        rating = response.json()
        return rating
