import requests, argparse, os.path, json

parser = argparse.ArgumentParser(description='Search GitHub repositories')
parser.add_argument('-v', '--value', type=str, help='Input search query')
parser.add_argument('-f', '--file', type=str, help='Output file')
args = parser.parse_args()  # Парсинг аргументов командной строки
value, output = args.value, args.file
assembly_sort = 'stars'
order = 'desc'


def check_path(path):
    if os.path.splitext(output)[1] != '.json':
        raise Exception("Not a *.json file.")
    elif os.path.exists(path):
        print("Файл с таким названием уже существует.\nХотите ли вы перезаписать его? (Y/N):")
        x = input()
        if x == "N":
            exit()
        elif x == "Y":
            return True
        else:
            raise Exception("Unexcepted error.")
    else:
        return True


def get_info(per_page, page):
    return requests.get(
        'https://api.github.com/search/repositories',
        params={'q': value,
                'assembly&sort': assembly_sort,
                'order': order,
                'per_page': per_page,
                'page': page},
    ).json()


def write_file():
    x = open(output, "w")
    for i in range(1, 11):
        response = get_info(100, i)
        info = json.dumps(response.get("items"), indent=4, separators=(", ", ": "))
        x.write(info)
    x.close()


if check_path(output):
    write_file()
