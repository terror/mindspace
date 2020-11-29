import click
from .commands import init, open, new, link, home, rm, rmlink
from .utils import Utils

commands = [
    init.init,
    new.new,
    open.open,
    link.link,
    home.home,
    rm.rm,
    rmlink.rmlink
]


@click.group()
@click.pass_context
def cli(ctx):
    """
    Entry point for the CLI.

    :param ctx: context object for subcommands
    """
    ctx.ensure_object(dict)
    ctx.obj["config"] = Utils.load_config()


for command in commands:
    cli.add_command(command)


if __name__ == "__main__":
    cli(obj={})
