from sqlalchemy import select
from sqlalchemy.orm import Session


from .. models import Genre


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
        retutn self.session.execute(stmt).scalars().all()


    def get_genre_by_name(self, name: str) -> Genre | None:
        stmt = select(Genre).where(Genre.name == name)
        return self.session.execute(stmt).scalar_one_or_none()