import click
import re
import typing


def handle_var_options(ctx, param, value) -> typing.Dict[str, str]:
    result = {}

    for v in value:
        fmt = "^([a-zA-Z0-9_]*)=([a-zA-Z0-9_]*)$"
        if not re.search(fmt, v):
            raise click.BadParameter("k/v param was invalid: '{}' but expected: '<key>=<value>'".format(value))

        (k, v) = v.split("=")
        result[k.strip()] = v.strip()

    return result


def handle_var_file_option(ctx, param, value) -> typing.Dict[str, str]:
    return {}
