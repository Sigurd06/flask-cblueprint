from flask import Flask
from flask.cli import AppGroup

from flask_cblueprint.commands.create_blueprint import create_blueprint_command
from flask_cblueprint.commands.list_blueprint import list_blueprints_command

class FlaskCBlueprint:
    def __init__(self, app: Flask | None = None) -> None:
        
        self.__app_cli: AppGroup = AppGroup('app')

        if app is not None:
            self.init_app(app)

    def __add_command(self):
        self.__app_cli.add_command(create_blueprint_command)
        self.__app_cli.add_command(list_blueprints_command)

    def init_app(self, app: Flask) -> None:
        self.__add_command()
        app.cli.add_command(self.__app_cli)
