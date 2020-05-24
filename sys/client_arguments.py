import re
import sys


def get_cli_args():
    """
    Returns a dictionary of arguments passed to through the CLI.
    """

    args = {}

    for arg in sys.argv[1:]:
        var = re.search("--(\\w*)", arg)
        var = var.group(1)
        value = re.search("=(.*)", arg)
        value = value.group(1) if value else None
        args[var] = value

    return args
