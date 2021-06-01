import requests, argparse, os.path, json

parser = argparse.ArgumentParser(description='Search GitHub repositories')
parser.add_argument('-v', '--value', type=str, help='Input search query')
parser.add_argument('-f', '--file', type=str, help='Output file')
args = parser.parse_args()  # Парсинг аргументов командной строки
value, output = args.value, args.file

assembly_sort = 'stars'
order = 'desc'

if os.path.exists(output):  # Проверка на существование файла с таким же названием
    print(f"Файл с таким названием уже существует.\nХотите ли вы перезаписать его? (Y/N):")
    if input() == "N":
        exit()

response = requests.get(
    'https://api.github.com/search/repositories',  # GET-запрос
    params={'q': value,                         # Текст запроса
            'assembly&sort': assembly_sort,              # Сортировка по звёздам
            'order': order},                      # Сортировка в убывающем порядке
)

info = json.dumps(response.json(), indent=4, separators=(", ", ": "))
with open(output, "w") as x:  # Запись в файл
    x.write(info)

