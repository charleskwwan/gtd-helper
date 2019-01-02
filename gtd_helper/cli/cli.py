# cli/cli.py
#   CLI for gtd-helper

import argparse
import sys

from gtd_helper.cli import cmds
from gtd_helper.cli.utils import load_method
from gtd_helper.cli.utils import modules_in_pkg


CMDS_MODULE_PREFIX = 'gtd_helper.cli.cmds.{command}'


def add_subparser(command, subparsers):
    """ Execute the `add_subparser` method implemented by each command. Each
    command must implement the `add_subparser` command.
    """
    module_name = CMDS_MODULE_PREFIX.format(command=command)
    add_subparser_fn = load_method(module_name, 'add_subparser')
    add_subparser_fn(subparsers)


def get_argparser():
    """ Creates the argument parser with gtd_helper commands """
    parser = argparse.ArgumentParser(
        description='The all-in-one GTD helper to get you organized with your life',
    )

    subparsers = parser.add_subparsers(help='gtd-helper commands', dest='command')
    subparsers.required = True
    for command in sorted(modules_in_pkg(cmds)):
        add_subparser(command, subparsers)

    return parser


def main(argv=None):
    try:
        parser = get_argparser()
        args = parser.parse_args(argv)
        if args.command is None:
            parser.print_help()
            return_code = 0
        else:
            return_code = args.command(args)
    except KeyboardInterrupt:
        return_code = 1
    sys.exit(return_code)


if __name__ == '__main__':
    main()
