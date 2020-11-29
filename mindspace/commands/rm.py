import os
import click
from ..note import Note


@click.command("rm", short_help="Remove an existing note")
@click.argument("note", nargs=1, required=True)
@click.pass_context
def rm(ctx, note):
    """
    Removes an existing note in the mindspace directory
    """
    directory = ctx.obj["config"]["owner"]["dir"]
    note = Note(directory, note)
    os.remove(note.path)

    click.secho("Success! Removed {}".format(note.filename), fg="green")
