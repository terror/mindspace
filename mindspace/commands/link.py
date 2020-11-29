import click
from ..note import Note
from ..utils import Utils


@click.command("link", short_help="Link two notes")
@click.argument("note1", nargs=1, required=True)
@click.argument("note2", nargs=1, required=True)
@click.pass_context
def link(ctx, note1, note2):
    """
    Creates a link between two existing notes
    """
    directory = ctx.obj["config"]["owner"]["dir"]

    note1, note2 = Note(directory, note1), Note(directory, note2)

    if note1.filename == note2.filename:
        Utils.display_error(
            "Cannot create a link between a note and itself.", "yellow")

    with open(note1.path, "a") as file:
        file.write("[{}]({})\n".format(note2.filename, note2.filename))

    with open(note2.path, "a") as file:
        file.write("[{}]({})\n".format(note1.filename, note1.filename))

    click.secho("Success! {} <-> {}".format(note1.filename,
                                            note2.filename), fg="green")
