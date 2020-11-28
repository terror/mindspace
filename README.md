## mindspace

A command line note taking application paired with a sleek and modern user interface.

`mindspace` aims to implement the [Zettelkasten]() method of note taking while providing a static site to interface with the notes.

### Arguments

`init`: Initialize the mindspace

`new [note]`: Create a new note

`open [note]`: Open an existing note

`link [a, b]`: Link two notes together

### Config File

A `mindspace` is configured via a config file called `.mindspace.toml` located in your home directory.

Example config:
```toml
[owner]
name = "Liam"
dir = "/path/to/mindspace"
```
