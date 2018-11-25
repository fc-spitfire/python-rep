# Имеется набор файлов, каждый из которых, кроме последнего, 
# содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на 
# первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.

import requests

_url = open('C:\\Users\\ggusp\\Programming\\python\\parser\\dataset_3378_3.txt').readline().strip()
_file = requests.get(_url)

_stepik = 'https://stepic.org/media/attachments/course67/3.6.3/'

def _getText(url):
    if url.split()[0] == 'We':
        print(url)
    else:
        print(requests.get(_stepik+url).text.strip())
        _getText(requests.get(_stepik+url).text.strip())

_getText(_file.text.strip())