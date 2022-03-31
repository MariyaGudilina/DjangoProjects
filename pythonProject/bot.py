import requests
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content

tree = lxml.html.document_fromstring(html)
title = tree.xpath('/html/head/title/text()')

with open(title[0], 'w') as output_file:
    output_file.write(str(html))


my_tree = etree.parse('Welcome to Python.org', lxml.html.HTMLParser())

ul = my_tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')

for li in ul:
    a = li.find('a')
    time = li.find('time')
    print(time.get('datetime'), a.text)






#r = requests.get(
#   'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# делаем запрос на сервер по переданному адресу

#print(r.content)
#print(r.status_code)
'''
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json-ответ
texts = json.loads(r.content)  # делаем из полученных байтов Python-объект для удобной работы

print(texts[1])

print(type(texts))  # проверяем тип сконвертированных данных

for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль, оставим только первые 50 символов.
    print(text[:50], '\n')


r = requests.get('https://api.github.com')

d = json.loads(r.content)

print(type(d))
print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json=json.dumps(data))  # отправляем пост-запрос
print(r.content)  # содержимое ответа и его обработка происходит так же, как и с ГЕТ-запросами, разницы никакой нету

'''