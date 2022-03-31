from random import randint


def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


def count(array, element):
    count = 0
    for i, a in enumerate(array):
        if a == element:
            count += 1
    return count

#array = list(map(int, input().split()))
#element = int(input())
#print(count(array, element))




# Алгоритмы бинарного поиска
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

def recursive_binary_seach(arr, target):
    mid = len(arr)//2
    if len(arr) == 1:
        print(arr)
        return mid
    elif arr[mid] == target:
        print(arr)
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_seach((arr[mid:]),target)
            return mid + callback_response
        else:
            print(arr)
            return recursive_binary_seach((arr[:mid]), target)


element = int(input("Введите число, которое будем искать:"))

array = [i for i in range(10, 100, 10)]  # 1,2,3,4,...

#array_random = [randint(0, 1) for i in range(1, 100)]

# запускаем алгоритм на левой и правой границе

print(recursive_binary_seach(array, element))

