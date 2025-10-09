# 01
# Напишите рекурсивную функцию для вычисления n-го числа
# Фибоначчи и проанализируйте стек вызовов для n = 5
import random
# 1. 5 разбивается на 4(в стек) и 3
# 2. 4 разбивается на 3(в стек) и 2
# 3. 3 разбивается на 2(в стек) и 1
# 4. 2 разбивается на 1(в стек) и 0
# 1 в стеке возвращает 1 и удалятеся из стека (4шаг)
# 0 вычисляется и возвращает 0 и удаляется из стека (4шаг)
# 4 шаг возвращает 1 + 0 = 1 и удаляется из стека
# 3 шаг возвращает 1 + 0 + 1 = 2 и удаляется из стека
# 2 шаг возвращает 1 + 0 + 1 + 1 + 0 = 3 и удаляется из стека
# 1 шаг возвращает 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 = 5 и удаляется из стека

# def fibonachi(num):
#     if num <= 1:
#         return num
#     else:
#         return (fibonachi(num - 1) + fibonachi(num - 2))
#
#
# print(fibonachi(5))

# 02
# Напишите рекурсивную функцию для нахождения максимального
# элемента в списке, используя подход "Разделяй и властвуй"

# from random import randint
#
# def max_elem(array):
#     if len(array) == 0:
#         return -1
#     if len(array) == 1:
#         return array[0]
#
#     middle_array = len(array) // 2
#     left_part = array[:middle_array]
#     right_part = array[middle_array:]
#
#     left_max = max_elem(left_part)
#     right_max = max_elem(right_part)
#
#     return left_max if left_max > right_max else right_max
#
#
# array = [(random.randint(1, 211)) for _ in range(23)]
# print(array)
# print(max_elem(array))

# 03
# Напишите функцию для реализации быстрой сортировки
# (QuickSort) с примером использования

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[len(array) // 2]
#
#     left_part = [i for i in array if i < pivot]
#     right_part = [i for i in array if i > pivot]
#     middle_part = [i for i in array if i == pivot]
#
#     return quick_sort(left_part) + middle_part + quick_sort(right_part)
#
#
# array = [(random.randint(1, 19)) for _ in range(27)]
# print(array)
# print(quick_sort(array))

# 04
# Проанализируйте время выполнения быстрой сортировки на
# списках различной длины (например, 10, 100, 1000 элементов)
# и сравните её с другими сортировками, такими как сортировка вставками

import time
import matplotlib.pyplot as plt

def buble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]

    left_part = [i for i in array if i < pivot]
    right_part = [i for i in array if i > pivot]
    middle_part = [i for i in array if i == pivot]

    return quick_sort(left_part) + middle_part + quick_sort(right_part)

list_size = [10, 100, 250, 500, 750, 1000]
time_bubble = []
time_selection = []
time_quick = []

for size in list_size:
    start = time.time()
    array = [(random.randint(1, 19)) for _ in range(size)]
    buble_sort(array)
    end = time.time()
    avg = (end - start) / 1000
    time_bubble.append(avg)

for size in list_size:
    start = time.time()
    array = [(random.randint(1, 19)) for _ in range(size)]
    selection_sort(array)
    end = time.time()
    avg = (end - start) / 1000
    time_selection.append(avg)

for size in list_size:
    start = time.time()
    array = [(random.randint(1, 19)) for _ in range(size)]
    quick_sort(array)
    end = time.time()
    avg = (end - start) / 1000
    time_quick.append(avg)

plt.figure(figsize=(7, 7))
plt.plot(list_size, time_bubble, color = 'pink')
plt.plot(list_size, time_selection, color = 'green')
plt.plot(list_size, time_quick, color = 'blue')
plt.xlabel('Размер списка')
plt.ylabel('Время (секунды)')
plt.title('Пузырьковая сортировка vs Сортировка выбором vs Быстрая сортировка')
plt.grid(True)
plt.show()
