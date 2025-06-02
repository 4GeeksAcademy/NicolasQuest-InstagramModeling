from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    """Follower"""

    followers: Mapped[list['Follower']] = relationship(
        'Follower', foreign_keys='Follower.user_to_id')
    following: Mapped[list['Follower']] = relationship(
        'Follower', foreign_keys='Follower.user_from_id')

    """Post"""
    post: Mapped[list['Post']] = relationship(
        'Post', foreign_keys='Post.user_id')


class Follower(db.Model):
    __tablename__ = 'follower'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    """Comment"""
    comment: Mapped[list['Comment']] = relationship(
        'Comment', foreign_keys='Comment.post_id')

    """Media"""
    media: Mapped['Media'] = relationship(
        'Media', foreign_keys='Media.post_id')


class Comment(db.Model):
    __tablename__ = 'commment'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(200))
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))


class Media(db.Model):
    __tablename__ = 'media'
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(120))
    url: Mapped[str] = mapped_column(String(100))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))


"""
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
"""
