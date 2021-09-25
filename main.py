from handlers.convertor_handler import ConvertHandler
from handlers.arguments_handler import ArgumentsHandler
import os

# example:
# python main.py -in test.avi

if __name__ == "__main__":
    args = ArgumentsHandler.get_arguments()
    if not len(args):
        exit(1)
    filename = args[0]
    c = ConvertHandler(filename)
    if not c:
        exit(1)
    c.convert()
