from pathlib import Path

from genesis.core.template_engine import TemplateEngine


class ProjectGenerator:
  def create(
    self,
    project_name: str,
    template: str = "python",
) -> bool:

        project = Path(project_name)

        if project.exists():
            return False

        (project / "src").mkdir(parents=True)
        (project / "tests").mkdir()

        engine = TemplateEngine()

        context = {
            "project_name": project_name,
            "project_slug": project_name.lower(),
        }

        files = [
            "README.md",
            "pyproject.toml",
            ".gitignore",
            ".editorconfig",
            "LICENSE",
        ]

        for file_name in files:
            content = engine.render(
                f"{template}/{file_name}",
                context,
            )

            (project / file_name).write_text(
                content,
                encoding="utf-8",
            )

        return True