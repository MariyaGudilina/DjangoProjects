# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import time

i = 10
while i != -1:
    print(i)
    time.sleep(1)
    i -= 1

print("Время")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # print(help(math))
    result = math.trunc(math.fmod(math.fabs(-10000000), 55) + 0.3)
    print(result)

'''
mx = 0
s = 0
x = int(input())
if x < 0:
    s = x

b = 7
b /= b

if x > mx:
    mx = x

print(s)
print(mx)


def is_leap_year(r):
    return (r % 400 == 0) or ((r % 4 == 0) and (r % 100 != 0))


x = int(input('Введите год: '))

print(is_leap_year(x))


list = [-5, 2, 4, 8, 12, -7, 5]
index_negative = None
for i, value in enumerate(list):
    if list[i] >= 0:
        print('Положительное число:', value)
    else:
        print('Отрицательное число:', value)
        index_negative = i
    print('----')
print("Конец цикла")
print()
print('Ответ:индекс последнего отрицательного элемента=', index_negative)


def char_frequency():
    text = """
    У лукоморья дуб зелёный;
    Златая цепь на дубе том:
    И днём и ночью кот учёный
    Всё ходит по цепи кругом;
    Идёт направо -- песнь заводит,
    Налево -- сказку говорит.
    Там чудеса: там леший бродит,
    Русалка на ветвях сидит;
    Там на неведомых дорожках
    Следы невиданных зверей;
    Избушка там на курьих ножках
    Стоит без окон, без дверей;
    Там лес и дол видений полны;
    Там о заре прихлынут волны
    На брег песчаный и пустой,
    И тридцать витязей прекрасных
    Чредой из вод выходят ясных,
    И с ними дядька их морской;
    Там королевич мимоходом
    Пленяет грозного царя;
    Там в облаках перед народом
    Через леса, через моря
    Колдун несёт богатыря;
    В темнице там царевна тужит,
    А бурый волк ей верно служит;
    Там ступа с Бабою Ягой
    Идёт, бредёт сама собой,
    Там царь Кащей над златом чахнет;
    Там русский дух... там Русью пахнет!
    И там я был, и мёд я пил;
    У моря видел дуб зелёный;
    Под ним сидел, и кот учёный
    Свои мне сказки говорил.
    """

    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # print(count)
    for char, value in count.items():
        print(f"Символ {char} встречается {value} раз")


# char_frequency()


def print_2_add_2():
    result = 2 + 2
    print(result)


# print_2_add_2()

def multiply(*nums):
    mul_ = 1
    for n in nums:
        mul_ *= n

    return mul_


print('Вывод:', multiply(2, 3, 4, 5))

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 5
b = 3 + 2
print(id(a) - id(b))

a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_before == list_id_after)

text = "The Zen of Python"

unique = set(text)

print("Количество уникальных символов: ", len(unique))
a = None
b = 0

if a and b:
    # проверка истинности обеих переменных
    print("Обе переменные истинные")
    print(a, b)

L = list(map(int, input().split()))
print(all(L))

L = list(map(int, input().split()))

print(not any(L))

text = input()  # получаем строку

last = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == last:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += last + str(count)  # иначе - записываем в результат
        last = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += last + str(count)  # и добавляем в результат последний символ
print(result)
'''

'''
def linear_solve(n, r):
    if n:
        return r / n
    elif not n and not r:  # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else:
        return "Нет корней"


print(linear_solve(0, 1))


# a*x**2 + b*x + c = 0 - общий вид уравнения
# D = b**2 - 4*a*c - дискриминант
# Если D<0, то уравнение не имеет вещественных корней
# Если D=0, то уравнение имеет один корень - x = -b/(2*a)
# Если D>0, то уравнение имеет два корня
# x1 = (-b - D**0.5)/(2*a)
# x2 = (-b + D**0.5)/(2*a)
#
# P.S. D**0.5 - равносильно извлечению квадратного корня

def discriminant_my(a, b, c):
    return b ** 2 - 4 * a * c


def roots_my(a, b, c):
    d = discriminant_my(a, b, c)
    if d < 0:
        return print("Уравнение не имеет вещественных корней")
    elif d == 0:
        x = -b / (2 * a)
        return print("Уравнение один корень", x)
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        return print("Уравнение имеет два корня", x1, x2)


L = list(map(float, input("Enter = ").split()))

roots_my(*L)
'''
'''
def min_list(K):
    if len(K) == 1:
        return K[0]
    return K[0] if K[0] < min_list(K[1:]) else min_list(K[1:])


print(min_list(L))


def mirror(a, res=0):
    return mirror(a // 10, res * 10 + a % 10) if a else res


print(mirror(4578))


def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)


last = 0
e = 2.718
for a in e():
    # e() - генератор
    if (a - last) < 0.00000001:  # ограничение на точность
        print(a)
        break
        # после достижения которого - завершаем цикл
    else:
        last = a  # иначе - присваиваем новое значение


def e():
    n = 1

    while True:
        yield (1 + 1 / n) ** n
        n += 1


def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")

    return wrapper


def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещен")

    return wrapper


@is_auth
def from_db():
    print("some data from database")

from_db()


USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")


@is_auth
@has_access
def from_db():
    print("some data from database")


from_db()


def filter(func, cont):
    outp = []
    for x in cont: # проходим циклом по итерируемому объекту
        if func(x): # проверяем условие для каждого элемента
            outp.append(x) # если True, добавляем в новый список
    return outp


def positive(x):
    return x % 2 == 0

t = [-2, -1, 0, 1, -3, 2, -3]

print(filter(positive, t))

a_list = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a_list)))
'''


def par_checker(string):
    stack = []  # инициализируем стек

    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка,
            stack.append(s)  # добавляем ее в стек
        elif s == ")":
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0


print(par_checker("(((999)))"))

pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(par_checker_mod("(([(999)))"))


# Создадим класс Queue - нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди

    def is_empty(self):  # очередь пуста?
        # да, если указатели совпадают и в них содержится ноль
        return self.head == self.tail and self.tasks[self.head] == 0

    def size(self):  # получаем размер очереди
        if self.is_empty():  # если она пуста
            return 0  # возвращаем ноль
        elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
            return self.max_size  # значит очередь заполнена
        elif self.head > self.tail:  # если хвост очереди сместился в начало списка
            return self.max_size - self.head + self.tail
        else:  # или если хвост стоит правее начала
            return self.tail - self.head

    def add(self):
        self.task_num += 1  # увеличиваем порядковый номер задачи
        self.tasks[self.tail] = self.task_num  # добавляем его в очередь
        print(f"Задача №{self.tasks[self.tail]} добавлена")

        # увеличиваем указатель на 1 по модулю максимального числа элементов
        # для зацикливания очереди в списке
        self.tail = (self.tail + 1) % self.max_size

    def show(self):  # выводим приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} в приоритете")

    def do(self):  # выполняем приоритетную задачу
        print(f"Задача №{self.tasks[self.head]} выполнена")
        # после выполнения зануляем элемент по указателю
        self.tasks[self.head] = 0
        # и циклично перемещаем указатель
        self.head = (self.head + 1) % self.max_size


size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty":
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add":
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do":
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit":
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")


