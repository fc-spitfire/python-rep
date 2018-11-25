#Напишите программу, которая считывает текст из файла 
#(в файле может быть больше одной строки) и выводит 
#самое частое слово в этом тексте и через пробел то, 
#сколько раз оно встретилось. Если таких слов несколько, 
#вывести лексикографически первое (можно использовать 
#оператор < для строк).

#Слова, написанные в разных регистрах, считаются одинаковыми.

_input = open('C:\\Users\\ggusp\\Programming\\python\\parser\\dataset_3363_3.txt')

s = []
for line in _input:
    s += line.lower().split()
_d = {}

for i in s:
    if i not in _d:
        _d[i] = 1
    else:
        _d[i] += 1

max = 0
for key in _d:
    if _d[key] > max:
        max = _d[key]

d = []
for key in _d:
    if _d[key] == max:
        d.append(key)

d.sort()
print(d[0], max)