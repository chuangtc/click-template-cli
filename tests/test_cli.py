from click.testing import CliRunner
from click_template_cli.cli import main

def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(main, ['--name', 'World'])
    assert result.exit_code == 0
    assert 'Hello, World!' in result.output

def test_custom_name():
    runner = CliRunner()
    result = runner.invoke(main, ['--name', 'Alice'])
    assert result.exit_code == 0
    assert 'Hello, Alice!' in result.output
