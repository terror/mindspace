import os
import click
from .utils import Utils


class Note:
    """
    Note class. Responsible for handling note path
    validation and fetching filenames

    :param directory: directory of the mindspace
    :param name: name of the note
    """

    def __init__(self, directory, name):
        self.directory = directory
        self.name = name
        self.filename = self.filename()
        self.path = self.path()

    def filename(self):
        """
        Fetches the filename of the note based on its name.
        Prompts the user with options if there exists multiple
        notes with the same name.

        :return: note filename or error message
        """
        notes = {}

        for file in os.listdir(self.directory):
            parts = file.split("-")
            parts[len(parts) - 1] = parts[len(parts) - 1][:-3]
            notes[file] = " ".join(parts[1:])

        if not self.duplicate_notes(notes):
            for id, name in notes.items():
                if name == self.name:
                    return id
        else:
            click.secho(
                "There exists more than one note with name: '{}'".format(
                    self.name),
                fg="yellow",
            )
            for id, name in notes.items():
                if name == self.name:
                    choice = input("Did you mean: {}? [y/n]: ".format(id))
                    if choice == "y" or choice == "Y":
                        return id

        Utils.display_error("Note not found.", fg="red")

    def duplicate_notes(self, notes):
        """
        Checks if there exist duplicate notes in mindspace directory

        :param notes: notes dict
        :rtype: bool
        """
        return list(notes.values()).count(self.name) > 1

    def path(self):
        """
        Constructs the path based on the mindspace directory
        and filename

        :rtype: str or error
        """
        path = os.path.join(self.directory, self.filename)

        if not os.path.exists(path):
            Utils.display_error("Note does not exist.", "red")

        return os.path.join(self.directory, self.filename)
