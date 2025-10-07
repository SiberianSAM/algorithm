# Эффективность поиска в отсортированных структурах данных
# Значительное сокращение времени поиска по сравнению с линейным поиском
# Временная сложность: O (log n),где n—количество элементов в массиве
# Пространственная сложность: O(1),так как используется фиксированное количество дополнительной памяти

# №1 №2

# import random
#
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         middle = (low + high) // 2
#         if arr[middle] == target:
#             return middle
#         elif arr[middle] < target:
#             low = middle + 1
#         else:
#             high = middle - 1
#     return -1
#
# array = []
# target = int(input(f'Введите число для поиска:'))
# for _ in range(25):
#     array.append(random.randint(1, 100))
# array = sorted(array)
#
# print(array)
# print(binary_search(array, target))

# № 3 № 4

import matplotlib.pyplot as plt
import random, time

def search_index(arr, value):
    for i in range(0, len(arr)):
        if arr[i] == value:
            return i
    return -1

sizes = [100, 1000, 10000, 100000]
times_index = []

for size in sizes:
    start_time = time.time()
    arr = [random.randint(1, 100) for _ in range(0, size)]
    search_index(arr, value=50)
    end_time = time.time()
    avg_time = (end_time - start_time) / 1000
    times_index.append(avg_time)


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

array = [random.randint(1, 100) for _ in range(100)]
array = sorted(array)
target = 11

times_binary = []

for size in sizes:
    test_arr = list(range(size))
    start_time = time.time()
    for _ in range(1000):
        binary_search(test_arr, size // 2)
    end_time = time.time()
    times_binary.append((end_time - start_time) / 1000)

plt.figure(figsize=(5, 5))
plt.plot(sizes, times_binary, 'bo-', linewidth=2)
plt.plot(sizes, times_index, 'ro-', linewidth=2)
plt.xlabel('Размер списка')
plt.ylabel('Время (секунды)')
plt.title('Бинарный поиск vs Линейный поиск')
plt.grid(True)
plt.show()