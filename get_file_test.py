import requests

_url = open('C:\\Users\\ggusp\\Programming\\python\\parser\\dataset_3378_2.txt').readline().strip()
_file = requests.get(_url)

c = 0
for line in _file.text.splitlines():
    c += 1

print(c)