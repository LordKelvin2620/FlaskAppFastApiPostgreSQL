from config import config
from flask import Flask
from routes import Movie

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page <h1>", 404

if __name__ == '__main__':
    app.register_blueprint(Movie.main, url_prefix='/api/movies')
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()