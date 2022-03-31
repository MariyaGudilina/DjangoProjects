G = {
    "Адмиралтейская": {"Садовая": 4},
    "Садовая": {
        "Сенная площадь": 4,
        "Спасская": 3,
        "Адмиралтейская": 4,
        "Звенигородская": 5},
    "Сенная площадь": {
        "Садовая": 4,
        "Спасская": 4},
    "Спасская": {
        "Садовая": 3,
        "Сенная площадь": 4,
        "Достоевская": 6},
    "Звенигородская": {
        "Пушкинская": 3,
        "Садовая": 5},
    "Пушкинская": {
        "Звенигородская": 3,
        "Владимирская": 4},
    "Владимирская": {
        "Достоевская": 3,
        "Пушкинская": 4},
    "Достоевская": {
        "Владимирская": 3,
        "Спасская": 6}
}

D = {k: 100 for k in G.keys()}  # расстояния
start_k = 'Адмиралтейская'  # стартовая вершина
D[start_k] = 0  # расстояние от нее до самой себя равно нулю
U = {k: False for k in G.keys()}  # флаги просмотра вершин
P = {k: None for k in G.keys()}

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])
    # print(f'KKK' + min_k)
    for v in G[min_k].keys():  # проходимся по всем смежным вершинам
        # print(f'VVV' + str(v))
        # D[v] = min(D[v], D[min_k] + G[min_k][v])  # минимум
        if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
            D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
            P[v] = min_k  # и записываем как предок
    U[min_k] = True  # просмотренную вершину помечаем

pointer = 'Владимирская'  # куда должны прийти
while pointer is not None:  # перемещаемся, пока не придем в стартовую точку
    print(pointer)
    pointer = P[pointer]


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию


# создаем корень и его потомки /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

#node_root.post_order()


class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''
        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def push_first(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def push_last(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный

    def __iter__(self):  # объявляем класс как итератор
        self.current = self.first  # в текущий элемент помещаем первый
        return self  # возвращаем итератор

    def __next__(self):  # метод перехода
        if self.current is None:  # если текущий стал последним
            raise StopIteration  # вызываем исключение
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next  # совершаем переход
            return node  # и возвращаем сохраненный

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count


LL = LinkedList()

LL.push_last(1)
LL.push_first(2)
LL.push_last(3)
LL.popright()
LL.push_first(4)
LL.push_last(5)
LL.popleft()

print(LL.__len__())








array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

num = 0
for i in range(len(array)): # проходим по всему массиву
    num += 1
    idx_min = i # сохраняем индекс предположительно минимального элемента
    for j in range(i+1, len(array)):
        if array[j] < array[idx_min]:
                idx_min = j
                num += 1
        if i != idx_min: # если индекс не совпадает с минимальным, меняем
                num += 1
                array[i], array[idx_min] = array[idx_min], array[i]

num1 = 0
array1 = [2, 3, 1, 4, 6, 5, 9, 8, 7]
for i in range(1, len(array1)):
    x = array1[i]
    idx = i
    num1 += 1
    while idx > 0 and array1[idx-1] > x:
        array1[idx] = array1[idx-1]
        idx -= 1
        num1 += 1
    array1[idx] = x

print(num1)
print(array1)
