import pymongo
from environs import Env
from datetime import datetime
from app.exceptions.posts_exceptions import InvalidPost, PostNotFound
import ipdb

env = Env()
env.read_env()

client = pymongo.MongoClient(f"mongodb://{env('DATABASE_URL')}:{int(env('DATABASE_PORT'))}/")

db = client['kenzie']

class Post:
    def __init__(self, title: str, author: str, tags: list, content: str):
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
        self.id = Post.last_id() + 1
        self.created_at = datetime.utcnow()
        self.update_at = None


    def save(self):
        new_post = db.post.insert_one(self.__dict__)
        
        if not new_post:
            raise InvalidPost

        post = db.post.find_one({'id': self.id})
        del post['_id']
        del post['update_at']
        return post
            
        
    @staticmethod
    def update(old_data, update_data):
        update_data['update_at'] = datetime.utcnow()
        update_post = db.post.update_one({'id': old_data['id']}, {'$set': update_data})
    
        if not update_post:
            raise PostNotFound

        post = Post.get_by_id(old_data['id'])
        return post


    @staticmethod
    def get_all_posts():
        all_posts = list(db.post.find())
        for post in all_posts:
            del post['_id']
            if not post['update_at']:
                del post['update_at']
        return all_posts


    @staticmethod
    def get_by_id(id: int):
        post = db.post.find_one({'id': id})
        
        if not post:
            raise PostNotFound

        del post['_id']
        if not post['update_at']:
            del post['update_at']
        return post


    @staticmethod
    def last_id():
        data_list = Post.get_all_posts()

        if len(data_list) > 0:
            last_id = data_list[-1]['id']
            return last_id

        return 0


    @staticmethod
    def delete(id: int):
        post = db.post.find_one_and_delete({'id': id})

        if not post:
            raise PostNotFound

        del post['_id']
        return post