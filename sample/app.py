from flask_cblueprint import FlaskCBlueprint
from flask import Flask
from dotenv import load_dotenv
from sample.config import config

load_dotenv()


def create_app():
    """
    It creates a Flask app and initializes the FlaskCBlueprint extension.
    :return: The app object is being returned.
    """
    app = Flask(__name__)

    # Loading the configuration from the config.py file.
    app.config.from_object(config)

    # Initializing the FlaskCBlueprint extension.
    flask_cblueprint = FlaskCBlueprint()
    flask_cblueprint.init_app(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()