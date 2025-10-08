# 01
# Напишите рекурсивную функцию для вычисления факториала числа n
import random
# def recursion(num):
#     if num == 1:
#         return 1
#     else:
#         return num * recursion(num - 1)
#
# print(recursion(10))

# 02
# Напишите рекурсивную функцию для вычисления суммы всех
# элементов в списке. Убедитесь, что у функции есть базовый случай

# from random import randint
#
# def recursion_sum(array):
#     if not array:
#         return 0
#     else:
#         return array[0] + recursion_sum(array[1:])
#
# array = [(random.randint(1, 25)) for _ in range(5)]
# print(recursion_sum(array))

# 03
# Напишите рекурсивную функцию для выполнения бинарного
# поиска элемента в отсортированном списке. Функция должна
# возвращать индекс найденного элемента или -1, если элемент не
# найден

# from random import randint
#
# def binary_search(array, low, high, target):
#     if high > low:
#         middle = (high - low) // 2
#         if array[middle] == target:
#             return middle
#         elif array[middle] < target:
#             return binary_search(array, middle + 1, high, target)
#         else:
#             return binary_search(array, low, middle - 1, target)
#     return -1
#
# array = sorted([(random.randint(1, 25)) for _ in range(8)])
# print(binary_search(array, 0, len(array) - 1, 7))

# 04
# Напишите класс Stack, который реализует основные операции
# стека: push, pop, is_empty и peek

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return 'Stack is empty!'

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Stack is empty!'

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push('Hello')
    s.push('My')
    s.push(4)
    s.push('Friend')
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.peek())
