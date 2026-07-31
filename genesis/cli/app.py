import click

from genesis.cli.create import create


@click.group()
def cli():
    """Genesis Framework CLI"""
    pass


@cli.command()
def version():
    """Show Genesis version"""
    click.echo("Genesis Framework v1.0.0")


cli.add_command(create)


if __name__ == "__main__":
    cli()