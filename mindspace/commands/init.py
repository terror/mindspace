import os
import click
from ..utils import Utils

data = """
[owner]
name = "Placeholder"
dir = "{}"
""".strip().format(
    os.getcwd()
)


@click.command("init", short_help="Initialize the Zettelkasten directory")
def init():
    """
    Creates and writes default config to config
    file in the home directory
    """
    write_default_config(
        open(os.path.expanduser(Utils.config_file()), "w+"), data)

    click.secho("Initialization complete!", fg="green")


def write_default_config(config, data):
    config.write(data)
