from click.testing import CliRunner
from mindspace import cli


def test_init():
    runner = CliRunner()

    result = runner.invoke(cli, ['init'])
    assert result.exit_code == 0
    assert result.output == 'Initialization complete!\n'
