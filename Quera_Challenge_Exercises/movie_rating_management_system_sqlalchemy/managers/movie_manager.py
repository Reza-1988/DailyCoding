from sqlalchemy import select
from sqlalchemy.orm import Session

from .. models import Movie, Genre





class MovieManager:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, title: str, release_year: int) -> Movie:
        movie = Movie(title=title, release_year=release_year)
        self.session.add(movie)
        self.session.commit()
        return movie

    def get(self, movie_id: int) -> Movie | None:
        return self.session.get(Movie, movie_id)

    def get_all(self):
        stmt = select(Movie)
        return self.session.execute(stmt).scalars().all()

    def add_genre(self, movie_id: int, genre: Genre) -> Movie:
        movie = self.session.get(Movie, movie_id)
        movie.genres.append(genre)
        self.session.commit()
        return movie


    def get_reviews(self, movie_id: int):
        movie = self.session.get(Movie, movie_id)
        return movie.reviews

    def get_average_rating(self, movie_id: int):
        movie = self.session.get(Movie, movie_id)

        if not movie.reviews:
            return None

        sum_rating = sum(review.rating for review in movie.reviews)
        return sum_rating / len(movie.reviews)
