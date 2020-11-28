import os
import toml
import click


class Utils:
    @staticmethod
    def check_config():
        return os.path.exists(Utils.config_file())

    @staticmethod
    def config_file():
        return os.path.expanduser("~/.mindspace.toml")

    @staticmethod
    def load_config():
        try:
            config = toml.load(Utils.config_file())
        except Exception as error:
            Utils.display_error("Error parsing config file: {}".format(error))

        return config

    @staticmethod
    def display_error(msg, fg):
        click.secho(msg, fg=fg)
        exit()
