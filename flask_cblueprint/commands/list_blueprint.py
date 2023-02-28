import click
from flask.cli import with_appcontext
from flask_cblueprint.config import BLUEPRINTS_DIRECTORY
from flask_cblueprint.utils.list import list_blueprints


@click.command("list-blueprints")
@with_appcontext
def list_blueprints_command():
    available_blueprints = list_blueprints(BLUEPRINTS_DIRECTORY)

    [click.echo(bp_name) for bp_name in available_blueprints]
