import random, time
from cProfile import label

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

sizes = [10, 100, 300, 500, 800, 1000]
times_bubble = []
times_selection = []

for size in sizes:
    start_time = time.time()
    array = [random.randint(1, 100) for _ in range(size)]
    buble_sort(array)
    end_time = time.time()
    avg_time = (end_time - start_time) / 1000
    times_bubble.append(avg_time)

for size in sizes:
    start_time = time.time()
    array = [random.randint(1, 100) for _ in range(size)]
    selection_sort(array)
    end_time = time.time()
    avg_time = (end_time - start_time) / 1000
    times_selection.append(avg_time)

plt.figure(figsize=(5, 5))
plt.plot(sizes, times_bubble, 'bo-', linewidth=2)
plt.plot(sizes, times_selection, 'ro-', linewidth=1)
plt.xlabel('Размер списка')
plt.ylabel('Время (секунды)')
plt.title('Пузырьковая сортировка vs Сортировка выбором')
plt.grid(True)
plt.show()