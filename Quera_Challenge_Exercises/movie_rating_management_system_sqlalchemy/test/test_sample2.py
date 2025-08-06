import unittest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from .. models import Base, Movie, Genre, Review, User
from .. managers.movie_manager import MovieManager
from .. managers.genre_manager import GenreManager
from .. managers.review_manager import ReviewManager
from .. managers.user_manager import UserManager


class TestManagerUpdateDelete(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()
        self.movie_manager = MovieManager(self.session)
        self.genre_manager = GenreManager(self.session)
        self.review_manager = ReviewManager(self.session)
        self.user_manager = UserManager(self.session)

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    def test_update_and_delete(self):
        # MovieManager
        movie = self.movie_manager.create("The Matrix", 1999)
        updated_movie = self.movie_manager.update(movie.id, {"title": "The Matrix Reloaded"})
        self.assertEqual(updated_movie.title, "The Matrix Reloaded")
        self.assertTrue(self.movie_manager.delete(movie.id))

        # GenreManager
        genre = self.genre_manager.create("Sci-Fi")
        updated_genre = self.genre_manager.update(genre.id, "Science Fiction")
        self.assertEqual(updated_genre.name, "Science Fiction")
        self.assertTrue(self.genre_manager.delete(genre.id))

        # ReviewManager
        user = self.user_manager.create("Alice", "alice@example.com")
        movie = self.movie_manager.create("Inception", 2010)
        review = self.review_manager.create(user.id, movie.id, 4, "Good movie!")
        updated_review = self.review_manager.update(review.id, {"rating": 5})
        self.assertEqual(updated_review.rating, 5)
        self.assertTrue(self.review_manager.delete(review.id))

        # UserManager
        user = self.user_manager.create("Bob", "bob@example.com")
        updated_user = self.user_manager.update(user.id, {"name": "Robert"})
        self.assertEqual(updated_user.name, "Robert")
        self.assertTrue(self.user_manager.delete(user.id))


if __name__ == "__main__":
    unittest.main()