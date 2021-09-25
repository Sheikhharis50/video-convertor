import argparse
from utils.helpers import log


class ArgumentsHandler:

    def get_arguments_map():
        return [
            dict(
                name="input",
                flag="--input",
                short_flag="-in",
                help="Input a filename",
                isRequired=True
            ),
        ]

    def set_arguments_parser():
        parser = argparse.ArgumentParser()
        map = ArgumentsHandler.get_arguments_map()
        for item in map:
            parser.add_argument(
                item['flag'],
                item['short_flag'],
                help=item['help']
            )
        return parser.parse_args(), map

    def get_arguments():
        args, map = ArgumentsHandler.set_arguments_parser()
        verified_args = []
        for obj in map:
            arg = getattr(args, obj['name'])
            if not arg and obj['isRequired']:
                log(obj['help'])
                return []
            verified_args.append(arg)
        return verified_args
