import click
import time
import os


@click.command("new", short_help="Create a new note")
@click.argument("note", nargs=1, required=True)
@click.pass_context
def new(ctx, note):
    directory = ctx.obj["config"]["owner"]["dir"]

    name = create(directory, note)

    click.secho(
        "Success! Created note: {} in directory: {}".format(
            name, directory
        ),
        fg="green",
    )

    click.edit(filename=os.path.join(directory, name))


def create(directory, note):
    name = str(int(time.time())) + \
        "".join(["-{}".format(i) for i in note.split()])

    with open(os.path.join(directory, name + ".md"), "w+") as file:
        parts = name.split("-")
        file.write("## {} {}## Links".format(" ".join(parts), "\n" * 5))

    return name + ".md"
