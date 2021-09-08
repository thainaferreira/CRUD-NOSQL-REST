import ipdb
from app.exceptions.posts_exceptions import InvalidPost, PostNotFound
from flask import Flask, request, jsonify
from app.models.post_model import Post

def init_app(app: Flask):

    @app.post('/create-post')
    def create_post():
        data = request.json

        try:
            post = Post(**data)
            new_post = post.save()
            return new_post, 201
        except InvalidPost:
            return {'message': 'Dados inválidos para a criação da publicação'}, 400

    
    @app.get('/get-posts')
    def get_all_posts():
        posts_list = Post.get_all_posts()
        return jsonify(posts_list), 200

    
    @app.get('/get-post/<int:id>')
    def get_post_by_id(id: int):
        try:
            post = Post.get_by_id(id)
            return post, 200
        except PostNotFound:
            return {'message': 'Publicação não encontrada'}, 404


    @app.patch('/update-post/<int:id>')
    def update_post_by_id(id: int):
        data = request.json

        try:
            post = Post.get_by_id(id)
            post_update = Post.update(post, data)
            return post_update, 200
        except PostNotFound:
            return {'message': 'Publicação não encontrada'}, 404
        except TypeError:
            return {'message': 'Dados inválidos para a atualização da publicação'}, 400

    
    @app.delete('/delete-post/<int:id>')
    def delete_post_by_id(id: int):
        try:
            post = Post.delete(id)
            return post, 200
        except PostNotFound:
            return {'message': 'Publicação não encontrada'}, 404