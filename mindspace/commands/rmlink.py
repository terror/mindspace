import click
from ..note import Note
from ..utils import Utils


@click.command("rmlink", short_help="Remove a link between two existing notes")
@click.argument("note1", nargs=1, required=True)
@click.argument("note2", nargs=1, required=True)
@click.pass_context
def rmlink(ctx, note1, note2):
    directory = ctx.obj["config"]["owner"]["dir"]

    note1, note2 = Note(directory, note1), Note(directory, note2)

    if not note1.valid_note() or not note2.valid_note():
        Utils.display_error("Invalid note provided", "red")

    flag, lines = [0]*2, []

    with open(note1.path, "r") as f:
        lines = f.readlines()

    for line in reversed(lines):
        if note2.filename in line:
            lines.remove(line)
            flag[0] = 1

    with open(note1.path, "w") as a:
        for line in lines:
            a.write(line)

    with open(note2.path, "r") as f:
        lines = f.readlines()

    for line in reversed(lines):
        if note1.filename in line:
            lines.remove(line)
            flag[1] = 1

    with open(note2.path, "w") as b:
        for line in lines:
            b.write(line)

    if sum(flag) == 2:
        click.secho("Success! Link between {} and {} removed.".format(
            note1.filename, note2.filename), fg="green")
    else:
        Utils.display_error("Link between {} and {} does not exist.".format(
            note1.filename, note2.filename), "red")
