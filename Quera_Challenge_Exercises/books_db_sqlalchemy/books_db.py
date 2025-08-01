from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column
import sqlalchemy as db

engine = create_engine("sqlite:///movie_rating_management_system_sqlalchemy.db")


class Base(DeclarativeBase):
    pass

class Publisher(Base):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    books: Mapped[List["Book"]] = relationship(back_populates="publisher")


class BookGanre(Base):
    __tablename__ = "bookganres"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    book_id: Mapped[int] = mapped_column(db.ForeignKey("books.id"))
    genre_id: Mapped[int] = mapped_column(db.ForeignKey("genres.id"))


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    author: Mapped[str]
    publication_date: Mapped[db.Date]

    publisher_id: Mapped[int] = mapped_column(db.ForeignKey("publishers.id"))
    publisher: Mapped["Publisher"] = relationship(back_populates='books')
    genres: Mapped[List["Genre"]] = relationship(secondary="bookganres", back_populates="books")


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    books: Mapped[List["Book"]] = relationship(secondary="book_genres", back_populates='genres')














Base.metadata.create_all(engine)