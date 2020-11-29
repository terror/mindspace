import os
import click
from ..note import Note
from ..utils import Utils


@click.command("open", short_help="Open an existing note")
@click.argument("note", nargs=1, required=True)
@click.pass_context
def open(ctx, note):
    directory = ctx.obj["config"]["owner"]["dir"]

    path = Note(directory, note).path

    if not os.path.exists(path):
        Utils.display_error("Note does not exist.")

    click.edit(filename=path)
