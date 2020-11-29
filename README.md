## mindspace

A command line note taking application paired with a sleek and modern user interface.

`mindspace` aims to implement the [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) method of note taking while providing a static site to interface with the notes.

### Usage

```
Usage: mindspace [OPTIONS] COMMAND [ARGS]...

  Entry point for the CLI.

  :param ctx: context object for subcommands

Options:
  --help  Show this message and exit.

Commands:
  home    Output mindspace directory
  init    Initialize the Zettelkasten directory
  link    Link two notes
  new     Create a new note
  open    Open an existing note
  rm      Remove an existing note
  rmlink  Remove a link between two existing notes
```

### Config File

A `mindspace` is configured via a config file called `.mindspace.toml` located in your home directory.

Example config:

```toml
[owner]
name = "Liam"
dir = "/path/to/mindspace"
```
