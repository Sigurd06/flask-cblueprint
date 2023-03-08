from setuptools import setup


from flask_cblueprint import __title__, __author__, __author_email__, __version__, __copyright__, __license__

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Opening the README.md file and assigning it to the variable `readme`.
readme = open("./README.md", "r")

# A setup function that is used to install the package.
setup(
    name=__title__,
    version= __version__,
    author= __author__,
    author_email= __author_email__,
    license= __license__,
    copyright= __copyright__,
    url='https://github.com/Sigurd06/flask-cblueprint/tree/main',
    download_url='https://github.com/Sigurd06/flask-cblueprint/tree/v0.1.0',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    keywords=['Flask'],
    install_requires=required
)