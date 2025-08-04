import unittest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from .. models import Base, Movie, User
from .. managers.movie_manager import MovieManager
from .. managers.user_manager import UserManager

class TestMovieRatingSystemModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        self.session = self.Session()
        self.movie_manager = MovieManager(self.session)
        self.user_manager = UserManager(self.session)

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

    def test_create_movie(self):
        movie = self.movie_manager.create('The Matrix', 1999)
        self.assertIsNotNone(movie.id)
        self.assertEqual(movie.title, 'The Matrix')
        self.assertEqual(movie.release_year, 1999)

        fetched_movie = self.session.execute(select(Movie).where(Movie.title == 'The Matrix')).scalar_one()
        self.assertEqual(fetched_movie.title, 'The Matrix')
        self.assertEqual(fetched_movie.release_year, 1999)

    def test_create_user(self):
        user = self.user_manager.create('Alice', 'alice@example.com')
        self.assertIsNotNone(user.id)
        self.assertEqual(user.name, 'Alice')
        self.assertEqual(user.email, 'alice@example.com')

        fetched_user = self.session.execute(select(User).where(User.email == 'alice@example.com')).scalar_one()
        self.assertEqual(fetched_user.name, 'Alice')



if __name__ == "__main__":
    unittest.main()
