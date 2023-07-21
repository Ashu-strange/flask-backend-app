from .models import Post
from .. import db


class PostController:
    @staticmethod
    def create_post(text, location, time):
        res = Post.create_post(text, location, time)
        return res

    def get_posts(location, page):
        res = Post.get_posts(location, page)
        return res
