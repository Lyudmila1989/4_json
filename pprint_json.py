import json
import sys


def load_data(json_filepath):
    with open(json_filepath) as json_file:
        return json.load(json_file)


def pretty_print_json(json_content):
    print(json.dumps(json_content, sort_keys=True,
                     indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        json_filepath = sys.argv[1]
    except IndexError as Error1:
        json_filepath = input("Input the path to file ")
    pretty_print_json(load_data(json_filepath))
