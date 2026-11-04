import click
import subprocess
import sys
from tutor import hooks

hooks.Filters.CONFIG_DEFAULTS.add_item(
    ("MYFIRSTPLUGIN_DEFAULT_THEME", "indigo")
)

THEMES = {
    "indigo": "#15376D",
    "pink": "#E91E63",
}


@click.group(name="themes")
def themes():
    """Manage Open edX themes."""
    pass


@themes.command(name="list")
def list_themes():
    """List available themes."""
    for name, color in THEMES.items():
        click.echo(f"{name}: {color}")


@themes.command(name="set")
@click.argument("theme", type=click.Choice(["indigo", "pink"]))
def set_theme(theme):
    """Switch the Open edX website theme."""
    color = THEMES[theme]

    commands = [
        ["config", "save", "--set", f"INDIGO_PRIMARY_COLOR={color}"],
        ["images", "build", "openedx", "mfe"],
        ["local", "restart"],
    ]

    for command in commands:
        click.echo(f"\nRunning: tutor {' '.join(command)}")
        result = subprocess.run(
            ["tutor"] + command,
            check=False
        )

        if result.returncode != 0:
            raise click.ClickException(
                f"Command failed: tutor {' '.join(command)}"
            )

    click.echo(f"\nTheme switched to {theme} ({color}).")


hooks.Filters.CLI_COMMANDS.add_item(themes)
