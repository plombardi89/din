import click
import din.cmd.util
import pathlib
import typing


@click.group(
    name="template",
    help="Template management tools"
)
def template() -> None:
    pass


@template.command(
    help="Render one or more templates"
)
@click.option(
    "--template", "-t", "template_",
    help="One or more templates to render",
    multiple=True,
    type=click.Path(dir_okay=True,
                    exists=True,
                    file_okay=True,
                    readable=True)
)
@click.option(
    "--output-dir",
    help="Directory where rendered templates should be placed",
    type=click.Path(dir_okay=True,
                    file_okay=False),
)
@click.option(
    "--var",
    help="Pass a variable to the template renderer",
    multiple=True,
    type=str,
    callback=din.cmd.util.handle_var_options,
)
@click.option(
    "--var-file",
    help="Pass a file with many variables to the template renderer",
    multiple=False,
    type=click.Path(dir_okay=False,
                    exists=True,
                    file_okay=True,
                    readable=True),
    callback=din.cmd.util.handle_var_file_option,
)
def render(template_: typing.List[pathlib.Path],
           output_dir: pathlib.Path,
           var: typing.Dict[str, str],
           var_file: typing.Dict[str, str]) -> None:

    # CLI vars have a higher precedence than file variables to allow overrides.
    merged_vars = {**var_file, **var}
