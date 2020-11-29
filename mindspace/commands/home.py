import click
from ..utils import Utils


@click.command("home", short_help="Output mindspace directory")
@click.pass_context
def home(ctx):
    if not Utils.check_config():
        Utils.display_error("Config file not found.", "red")

    print(ctx.obj["config"]["owner"]["dir"])
