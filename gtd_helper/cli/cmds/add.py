# cli/cmds/add.py
#   Implements the `add` command, which adds new 'stuff' for tracking

def add_subparser(subparsers):
    main_parser = subparsers.add_parser(
        'add',
        help='Add new stuff to get done',
        description=(
            'Whenever you encounter something new you needto get done, '
            "it's not a good idea to keep all of it in your head. "
            'Add it here so I can track it for you!'
        ),
    )
    main_parser.set_defaults(command=add_stuff)


def add_stuff(args):
    print('Hello World!')
