from sqlalchemy import DateTime
from .. import db
from ..utils.constants import POSTS_PER_PAGE


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    time = db.Column(DateTime, nullable=False)

    def create_post(text, loc, time):
        post = Post(text=text, location=loc, time=time)
        db.session.add(post)
        db.session.commit()
        return post

    def get_posts(location, page):
        post = Post.query.filter_by(location=location).offset(
            (page-1)*POSTS_PER_PAGE).limit(POSTS_PER_PAGE).all()
        return post
