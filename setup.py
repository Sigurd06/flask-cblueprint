from setuptools import setup
from flask_cblueprint import __title__, __author__, __author_email__, __version__, __copyright__, __license__

setup(
    name=__title__,
    __version__= __version__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    copyright=__copyright__,
    install_requires=[
        "Flask>=1.0.4",
        "Werkzeug>=1.0.1",
    ]
)