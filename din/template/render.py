import base64
import jinja2
import pathlib
import shutil
import typing


_UTF8 = "utf-8"


def render_template(env: jinja2.Environment,
                    name: str,
                    variables: typing.Dict[str, typing.Any]) -> str:

    return env.get_template(name).render(**variables)


def render_templates(source: pathlib.Path,
                     target: pathlib.Path,
                     variables: typing.Dict[str, typing.Any]) -> None:

    root = source if source.is_dir() else source.parent

    def b64encode(value: str):
        return base64.b64encode(value.encode(_UTF8)).decode(_UTF8)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(root), encoding=_UTF8, followlinks=False))
    env.filters["b64encode"] = b64encode

    if source.is_dir():
        if target.exists():
            shutil.rmtree(str(target))

        target.mkdir(exist_ok=True)

        for it in source.glob("**/*"):
            if it.is_file():
                rel_path = it.relative_to(source)
                rendered = render_template(env, str(rel_path), variables)
                outfile = target / rel_path

                out_dir = outfile.parent
                out_dir.mkdir(exist_ok=True, parents=True)

                with outfile.open("w") as f:
                    f.write(rendered)
