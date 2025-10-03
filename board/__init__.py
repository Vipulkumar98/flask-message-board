import os


from dotenv import load_dotenv
from flask import Flask

from board import database, pages, posts, errors


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, World!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True) 

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    database.init_app(app)

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    app.register_error_handler(404, errors.page_not_found)

    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")

    print(f"Using Database: {app.config.get('DATABASE')}")

    return app