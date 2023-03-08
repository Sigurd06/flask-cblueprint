from flask_cblueprint.flask_cblueprint import FlaskCBlueprint
# Importing the variables from the __about__.py file.
from .__about__ import (__version__, 
                        __title__,
                        __author__,
                        __author_email__,
                        __copyright__,
                        __license__,
                        __maintainer__)

# A list of all the things that are imported when you do `from flask_cblueprint import *`
__all__ = [
    '__version__',
    '__title__',
    '__author__',
    '__author_email__',
    '__copyright__',
    '__license__',
    '__maintainer__',
    'FlaskCBlueprint',
]
