from flask import Flask


# > The `Config` class is a subclass of the `object` class. It has a class attribute called
# `FLASK_CBLUEPRINTS_DIRECTORY` which is set to the string `sample`. It also has a static method
# called `init_app` which takes a `Flask` object as an argument
class Config(object):
    FLASK_CBLUEPRINTS_DIRECTORY = 'sample'

    @staticmethod
    def init_app(app: Flask):
        pass

config = Config()
