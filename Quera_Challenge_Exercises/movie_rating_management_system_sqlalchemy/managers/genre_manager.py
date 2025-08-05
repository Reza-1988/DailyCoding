from sqlalchemy import select, func
from sqlalchemy.orm import Session


from .. models import Genre, MovieGenre


class GenreManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str) -> Genre:
        genre = Genre(name=name)
        self.session.add(genre)
        self.session.commit()
        return genre

    def get(self, genre_id: int) -> Genre | None:
        genre = self.session.get(Genre, genre_id)
        return genre if genre else None


    def get_all(self):
        stmt = select(Genre)
        return self.session.execute(stmt).scalars().all()


    def get_genre_by_name(self, name: str) -> Genre | None:
        stmt = select(Genre).where(Genre.name == name)
        return self.session.execute(stmt).scalar_one_or_none()

    def update(self, genre_id: int, new_name: str) -> Genre | None:
        genre = self.session.get(Genre, genre_id)
        genre.name = new_name
        self.session.commit()
        return genre if genre else None

    def delete(self, genre_id: int) -> bool:
        genre = self.session.get(Genre, genre_id)
        if genre:
            self.session.delete(genre)
            self.session.commit()
            return True
        return False


    def get_genres_with_most_movies(self) -> list[tuple]:
        query = (self.session
            .query(Genre, func.count(MovieGenre.movie_id).label("movie_count"))
            .join(MovieGenre, Genre.id == MovieGenre.genre_id)
            .group_by(Genre.id)
            .order_by(func.count(MovieGenre.movie_id).desc())
        )
        return query.all()

    # alternative with new fashion way

    def get_genres_with_most_movies(self) -> list[tuple]:
        stmt = (
            select(Genre, func.count(MovieGenre.movie_id).label("movie_count"))
            .join(MovieGenre, Genre.id == MovieGenre.genre_id)
            .group_by(Genre.id)
            .order_by(func.count(MovieGenre.movie_id).desc())
        )
        return self.session.execute(stmt).all()

