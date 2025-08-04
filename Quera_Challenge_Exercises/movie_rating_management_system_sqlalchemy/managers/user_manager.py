from sqlalchemy import select, func
from sqlalchemy.orm import Session

from ..models import User, Review


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, email: str) -> User:
        user = User(name=name, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def get(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_all(self):
        stmt = select(User)
        return self.session.execute(stmt).scalars().all()

    def get_user_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.session.execute(stmt).scalar_one_or_none()

    def get_most_active_users(self, limit=5):
        stmt = (select(Review.user_id, func.count(Review.id).label("review_count"))
                .group_by(Review.user_id)
                .order_by(func.count(Review.user_id).desc())
                .limit(limit)
        )
        return self.session.execute(stmt).all()

