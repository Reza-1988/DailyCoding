from datetime import datetime
from sqlalchemy import select, func, update
from sqlalchemy.orm import Session

from .. models import Movie, Genre, Review, MovieGenre


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
        stmt = select(Review).where(Review.movie_id == movie_id)
        return self.session.execute(stmt).scalars().all()

    def get_average_rating(self, movie_id: int):
        stmt = select(func.avg(Review.rating)).where(Review.movie_id == movie_id)
        return self.session.execute(stmt).scalar_one_or_none()

    def update(self, movie_id: int, update_data: dict) -> Movie | None:
        movie = self.session.get(Movie, movie_id)
        if movie:
            stmt = update(Movie).where(Movie.id == movie_id).values(**update_data)
            self.session.commit()
            return movie
        return None

    def delete(self, movie_id: int) -> bool:
        movie = self.session.get(Movie, movie_id)
        if movie:
            self.session.delete(movie)
            self.session.commit()
            return True
        return False

    def remove_genre(self, movie_id: int, genre: Genre) -> Movie | None:
        movie = self.session.get(Movie, movie_id)
        if movie:
            movie.genres.remove(genre)
            self.session.commit()
            return movie
        return None

    def get_top_movies_by_rating(self, limit: int = 10) -> list[tuple]:
        stmt = (
            select(Movie, func.avg(Review.rating).label("average_rating") )
            .join(Review, Movie.id == Review.movie_id)
            .group_by(Movie.id)
            .order_by(func.avg(Review.rating).desc())
            .limit(limit)
        )
        return self.session.execute(stmt).all()

    def get_movies_by_genre(self, genre_name: str) -> list[Movie]:
        pass


    def get_top_rated_movies_by_genre(self):
        pass
