from sqlalchemy import select
from sqlalchemy.orm import Session

from .. models import Review



class ReviewManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, movie_id: int, user_id: int, rating: int, comment: str = None) -> Review:
        pass

    def get(self, review_id: int) -> Review | None:
        pass

    def get_all(self):
        pass

    def get_reviews_by_user(self, user_id: int):
        pass

    def get_latest_reviews_for_movie_by_time(self, movie_id: int, limit: int = 5):
        pass

    def get_highest_rated_reviews(self, movie_id: int, limit: int = 5):
        pass

    def get_average_rating_by_user(self):
        pass