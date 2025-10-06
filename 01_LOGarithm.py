# Алгоритм последовательно проверяет каждый элемент списка.
# Когда элемент отсутствует или находится в конце, необходимо проверить все n элементов,
# что дает линейную зависимость времени выполнения от размера входных данных.

# №1

# def search_index(arr, value):
#     for i in range(0, len(arr)):
#         if arr[i] == value:
#             return i
#     return -1
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# value = 2
# print(search_index(arr, value))

# № 2

# import random
#
# arr = []
# for _ in range(0, 100):
#     num = random.randint(1, 100)
#     arr.append(num)
#
# def search_index(arr, value):
#     for i in range(0, len(arr)):
#         if arr[i] == value:
#             return i
#     return -1
#
# print(search_index(arr, 10))

# №3

import random, time
import matplotlib.pyplot as plt

def search_index(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return i
    return -1

sizes = [10, 100, 1000]
times = []

for size in sizes:
    start_time = time.time()
    arr = [random.randint(1, 100) for _ in range(0, size)]
    search_index(arr, value=50)
    end_time = time.time()
    avg_time = (end_time - start_time) / 1000
    times.append(avg_time)

plt.figure(figsize=(5, 5))
plt.plot(sizes, times, 'ro-', linewidth=1)
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (секунды)')
plt.title('Линейный поиск: время vs размер списка')
plt.grid(True)
plt.show()


