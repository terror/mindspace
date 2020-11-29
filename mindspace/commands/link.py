import click
from ..utils import Utils
from ..note import Note


@click.command("link", short_help="Link two notes")
@click.argument("note1", nargs=1, required=True)
@click.argument("note2", nargs=1, required=True)
@click.pass_context
def link(ctx, note1, note2):
    directory = ctx.obj["config"]["owner"]["dir"]

    note1, note2 = Note(directory, note1), Note(directory, note2)

    if not note1.valid_note() or not note2.valid_note():
        Utils.display_error("Invalid note provided", "red")

    with open(note1.path, "a") as file:
        file.write("\n[{}]({})".format(note2.filename, note2.filename))

    with open(note2.path, "a") as file:
        file.write("\n[{}]({})".format(note1.filename, note1.filename))

    click.secho("Success! {} <-> {}".format(note1.filename,
                                            note2.filename), fg="green")
