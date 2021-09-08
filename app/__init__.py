from flask import Flask
from app.views import post_views

def create_app():
    app = Flask(__name__)

    post_views.init_app(app)

    return app