import os
from .utils import Utils


class Note:
    def __init__(self, directory, name):
        self.directory = directory
        self.name = name
        self.filename = self.filename()
        self.path = self.path()

    def filename(self):
        notes = {}

        for file in os.listdir(self.directory):
            parts = file.split("-")
            parts[len(parts) - 1] = parts[len(parts) - 1][:-3]
            notes[file] = " ".join(parts[1:])

        if self.duplicate_notes(notes):
            for id, name in notes.items():
                if name == self.name:
                    print(id)

            Utils.display_error(
                "There exists more than one note with name: '{}'".format(
                    self.name),
                fg="yellow",
            )

        for id, name in notes.items():
            if name == self.name:
                return id

        Utils.display_error("Note not found.", fg="red")

    def duplicate_notes(self, notes):
        return list(notes.values()).count(self.name) > 1

    def valid_note(self):
        return os.path.exists(os.path.join(self.directory, self.filename))

    def path(self):
        return os.path.join(self.directory, self.filename)
