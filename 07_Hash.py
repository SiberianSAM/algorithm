# 01
# Напишите класс HashTable, который реализует основные
# операции хеш-таблицы: insert (вставка элемента), search
# (поиск элемента) и delete (удаление элемента

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
#
#     def hash_func(self, key):
#         return hash(key) % self.size
#
#     def insert(self, key, value):
#         index = self.hash_func(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key, value])
#
#     def search(self, key):
#         index = self.hash_func(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None
#
#     def delete(self, key):
#         index = self.hash_func(key)
#         for i, pair in enumerate(self.table[index]):
#             if pair[0] == key:
#                 del self.table[index][i]
#                 return True
#         return False
#
#
# hT = HashTable(15)
# hT.insert("Games", 25)
# hT.insert("Others", 5)
# hT.insert("Films", 30)
# hT.insert("Books", 1)
# print(hT.search("Games"))
# print(hT.search("Books"))
# print(hT.search("Others"))
# hT.delete('Books')
# print(hT.search('Books'))

# 02
# Добавьте в класс HashTable метод resize, который увеличивает
# размер хеш-таблицы вдвое и перераспределяет все элементы.
# Протестируйте работу метода на примере хеш-таблицы
# с начальным размером 5, добавив в неё 10 элементов

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
#
#     def hash_func(self, key):
#         return hash(key) % self.size
#
#     def insert(self, key, value):
#         index = self.hash_func(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key, value])
#
#     def search(self, key):
#         index = self.hash_func(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None
#
#     def delete(self, key):
#         index = self.hash_func(key)
#         for i, pair in enumerate(self.table[index]):
#             if pair[0] == key:
#                 del self.table[index][i]
#                 return True
#         return False
#
#     def resize(self):
#         old_table = self.table
#
#         self.size = self.size * 2
#         self.table = [[] for _ in range(self.size)]
#         for i in old_table:
#             for pair in i:
#                 self.insert(pair[0], pair[1])
#
#     def display(self):
#         print(f"Размер таблицы: {self.size}")
#         for i, couples in enumerate(self.table):
#             if couples:
#                 print(f"Индекс {i}: {couples}")
#             else:
#                 print(f"Индекс {i}: пусто")
#
#
# hT = HashTable(5)
# hT.insert("Games", 25)
# hT.insert("Others", 5)
# hT.insert("Films", 30)
# hT.display()
# hT.resize()
# hT.display()

# 03
# Напишите функцию, которая принимает строку и возвращает
# её хеш-значение. Для этого используйте простой алгоритм:
# сложение ASCII-кодов всех символов строки

# def hash_string(s):
#     hash_value = 0
#     for char in s:
#         hash_value += ord(char)
#     return hash_value
#
#
# s = 'Hello my friend! You just got the hash of the string'
# print(hash_string(s))

# 04
# Используйте написанную хеш-функцию для создания словаря,
# в котором ключами являются строки, а значениями — их хешзначения.
# Реализуйте функции добавления элемента в словарь и поиска значения по ключу


class HashTable:
    def __init__(self):
        self.hash_dict = {}

    def display(self):
        print(f'{self.hash_dict}')

    def hash_string(self, s):
        hash_value = sum(ord(char) for char in s)
        self.hash_dict[s] = hash_value
        return hash_value

    def search(self, key):
        for keys in self.hash_dict:
            if keys == key:
                return self.hash_dict[key]
        return None


hash_t = HashTable()
hash_t.hash_string('My friend, you are a good neighbor!')
hash_t.hash_string('Hello word!')
hash_t.hash_string('1')
hash_t.hash_string('LabroKodabro')
hash_t.display()
print(hash_t.search('Hello word!'))
print(hash_t.search('TinkoFF'))





