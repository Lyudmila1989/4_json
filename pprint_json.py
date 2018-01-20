import json


def load_data(json_filepath):
    with open(json_filepath) as f:
        return json.load(f)


def pretty_print_json(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False))
    pass


if __name__ == '__main__':
    json_filepath = input("Input the path to the file: ")
    pretty_print_json(load_data(json_filepath))
