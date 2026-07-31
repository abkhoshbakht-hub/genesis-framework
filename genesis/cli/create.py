import click

from genesis.generators.project_generator import ProjectGenerator


@click.command()
@click.argument("project_name")
@click.option(
    "--template",
    default="python",
    help="Project template",
)
def create(project_name, template):
    """Create a new Genesis project."""

    generator = ProjectGenerator()

    if generator.create(project_name, template):
        click.echo(f"✅ Project '{project_name}' created successfully.")
        click.echo(f"📦 Template : {template}")
    else:
        click.echo(f"❌ Folder '{project_name}' already exists.")