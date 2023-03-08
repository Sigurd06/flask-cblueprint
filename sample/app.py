from flask_cblueprint import FlaskCBlueprint
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    """
    It creates a Flask app and initializes the FlaskCBlueprint extension.
    :return: The app object is being returned.
    """

    app = Flask(__name__)

    flask_cblueprint = FlaskCBlueprint()
    flask_cblueprint.init_app(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()