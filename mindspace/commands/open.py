import click
from ..note import Note


@click.command("open", short_help="Open an existing note")
@click.argument("note", nargs=1, required=True)
@click.pass_context
def open(ctx, note):
    """
    Opens an existing note in the mindspace directory
    """
    directory = ctx.obj["config"]["owner"]["dir"]
    note = Note(directory, note)
    click.edit(filename=note.path)
