from flask import Flask, jsonify

from config import (
    SECRET_KEY,
    MAX_CONTENT_LENGTH,
    APP_TITLE
)

from services.database import initialize_database
from routes.main_routes import main
from routes.api_routes import api


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

    app.register_blueprint(main)
    app.register_blueprint(api)

    initialize_database()

    @app.errorhandler(413)
    def file_too_large(error):
        return jsonify({
            "error": "File is too large. Maximum size is 10 MB."
        }), 413

    @app.context_processor
    def inject_title():
        return {"app_title": APP_TITLE}

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )