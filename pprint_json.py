import json
import sys


def load_data(json_filepath):
    with open(json_filepath) as json_file:
        return json.load(json_file)


def pretty_print_json(json_content):
    print(
        json.dumps(
            json_content,
            sort_keys=True,
            indent=4,
            ensure_ascii=False
        )
    )


if __name__ == '__main__':
    try:
        pretty_print_json(load_data(sys.argv[1]))
    except IndexError:
        print("No file name specified")  
    except IOError as err2:
        print(err2)
