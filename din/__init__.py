import click

import din.cmd.template


@click.group(
    name="din"
)
def main():
    pass


main.add_command(din.cmd.template.template)
