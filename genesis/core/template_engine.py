from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class TemplateEngine:
    def __init__(self):

        templates = (
            Path(__file__).resolve().parent.parent
            / "templates"
        )

        self.env = Environment(
            loader=FileSystemLoader(templates),
            autoescape=False,
            keep_trailing_newline=True,
        )

    def render(self, template_name: str, context: dict) -> str:

        template = self.env.get_template(template_name)

        return template.render(**context)