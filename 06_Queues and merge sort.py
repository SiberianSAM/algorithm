# 01
# Напишите класс Queue, который реализует основные операции
# очереди: enqueue (добавление элемента), dequeue (удаление
# элемента), is_empty (проверка, пуста ли очередь) и peek (просмотр
# первого элемента в очереди)
import random
import time
from asyncio import current_task


# class Queue:
#     def __init__(self):
#         self.list = []
#
#     def enqueue(self, items):
#         self.list.append(items)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.list.pop(0)
#
#     def is_empty(self):
#         if len(self.list) == 0:
#             return True
#         else:
#             return False
#
#     def peek(self):
#         if not self.is_empty():
#             return self.list[0]
#         return None
#
# if __name__ == "__main__":
#     q = Queue()
#     print(q.is_empty())
#     q.enqueue(10)
#     q.enqueue(15)
#     print(q.peek())
#     q.enqueue(22)
#     print(q.is_empty())
#     print(q.peek())
#     q.dequeue()
#     print(q.peek())

# 02
# Смоделируйте простой процесс обработки задач в очереди.
# Допустим, у вас есть список задач, каждая из которых занимает
# определенное время на выполнение. Используйте очередь для
# обработки задач и выводите время, когда каждая задача будет завершена

# class Queue:
#     def __init__(self):
#         self.list = []
#
#     def enqueue(self, items):
#         self.list.append(items)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.list.pop(0)
#
#     def is_empty(self):
#         if len(self.list) == 0:
#             return True
#         else:
#             return False
#
#     def peek(self):
#         if not self.is_empty():
#             return self.list[0]
#         return None
#
# class Tasks:
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
#
#     def __str__(self):
#         return f'{self.name}, lead time - {self.duration}y.e.'
#
# def process_tasks(task_list):
#     q = Queue()
#     curent_time = 0
#     completed_tasks = []
#     for task in task_list:
#         q.enqueue(task)
#         print(f'Time: {curent_time}, {task} added in queue')
#
#     print(f'***Start of processing***')
#     while not q.is_empty():
#         current_task = q.dequeue()
#         start_time = curent_time
#         total_time = curent_time + current_task.duration
#
#         curent_time = total_time
#         completed_tasks.append((current_task.name, total_time))
#         print(f'Time: {start_time} - {current_task.name}')
#     print(f'***All tasks have been completed****')
#     return completed_tasks
#
#
# if __name__ == "__main__":
#     tasks = [
#         Tasks('Copying files in server', 10),
#         Tasks('Clear emails', 3),
#         Tasks('Updates programms', 9),
#         Tasks('Clear cookies', 1)
#     ]
#
#     completed = process_tasks(tasks)

# 03
# Напишите функцию для реализации сортировки слиянием
# (MergeSort) с примером использования

# def merge_sort(array):
#     if len(array) > 1:
#         middle = len(array) // 2
#         left_part = array[:middle]
#         right_part = array[middle:]
#
#         merge_sort(left_part)
#         merge_sort(right_part)
#         i = j = k = 0
#
#         while i < len(left_part) and j < len(right_part):
#             if left_part[i] < right_part[j]:
#                 array[k] = left_part[i]
#                 i += 1
#             else:
#                 array[k] = right_part[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_part):
#             array[k] = left_part[i]
#             i += 1
#             k += 1
#
#         while j < len(right_part):
#             array[k] = right_part[j]
#             j += 1
#             k += 1
#         return array
#
#
# array = [(random.randint(1, 23)) for _ in range(17)]
# print(f'Неотсортированный список: {array}')
# print(f'Сортировка слиянием: {merge_sort(array)}')

# 04
# Проанализируйте время выполнения сортировки слиянием на
# списках различной длины (например, 10, 100, 1000 элементов)
# и сравните её с другими сортировками, такими как сортировка пузырьком

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

def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_part = array[:middle]
        right_part = array[middle:]

        merge_sort(left_part)
        merge_sort(right_part)
        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            array[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            array[k] = right_part[j]
            j += 1
            k += 1
        return array

list_size = [10, 100, 250, 500, 750, 1000]
time_bubble = []
time_selection = []
time_quick = []
time_merge = []

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

for size in list_size:
    start = time.time()
    array = [(random.randint(1, 19)) for _ in range(size)]
    merge_sort(array)
    end = time.time()
    avg = (end - start) / 1000
    time_merge.append(avg)

plt.figure(figsize=(10, 6))
plt.plot(list_size, time_bubble, color = 'pink')
plt.plot(list_size, time_selection, color = 'green')
plt.plot(list_size, time_quick, color = 'blue')
plt.plot(list_size, time_merge, color = 'red')
plt.xlabel('Размер списка')
plt.ylabel('Время (секунды)')
plt.title('Пузырьковая сортировка vs Сортировка выбором vs Быстрая сортировка vs Сортировка слиянием')
plt.grid(True)
plt.show()