# 01
# Напишите класс BinaryTree, который реализует основные
# операции бинарного дерева: вставка (insert) и поиск (search)

# 02
# Напишите функцию для обхода бинарного дерева в ширину
# (Breadth-First Search, BFS)

# 03
# Напишите три функции для обхода бинарного дерева в глубину
# (Depth-First Search, DFS): прямой обход (preorder), симметричный
# обход (inorder) и обратный обход (postorder)

# from collections import deque
#
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, value):
#         new_node = TreeNode(value)
#
#         if self.root is None:
#             self.root = new_node
#             return
#
#         current = self.root
#         while True:
#             if value < current.value:
#                 if current.left is None:
#                     current.left = new_node
#                     return
#                 current = current.left
#             else:
#                 if current.right is None:
#                     current.right = new_node
#                     return
#                 current = current.right
#
#     def search(self, node):
#         if node:
#             self.search(node.left)
#             print(node.value, end=' ')
#             self.search(node.right)
#
#     def BFS(self, root):
#         if not root:
#             return
#         queue = deque([root])
#         while queue:
#             node = queue.popleft()
#             print(node.value, end=' ')
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#     def dfs_preorder(self, node):
#         if node:
#             print(node.value, end=' ')
#             self.dfs_preorder(node.left)
#             self.dfs_preorder(node.right)
#
#     def dfs_inorder(self, node):
#         if node:
#             self.dfs_inorder(node.left)
#             print(node.value, end=' ')
#             self.dfs_inorder(node.right)
#
#     def dfs_postorder(self, node):
#         if node:
#             self.dfs_postorder(node.left)
#             self.dfs_postorder(node.right)
#             print(node.value, end=' ')
#
#
#
# bt = BinaryTree()
# bt.insert(5)
# bt.insert(3)
# bt.insert(2)
# bt.insert(1)
# bt.insert(0)
# bt.insert(9)
# bt.insert(1)
# bt.search(bt.root)
# print('')
# bt.BFS(bt.root)
# print('')
# bt.dfs_preorder(bt.root)
# print('')
# bt.dfs_inorder(bt.root)
# print('')
# bt.dfs_postorder(bt.root)

# 04
# Напишите класс AVLTree, который наследует класс BinaryTree
# и добавляет операции балансировки при вставке элементов.
# Реализуйте методы для поворотов (left_rotate, right_rotate)
# и балансировки (rebalance)

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, node):
        if node:
            self.search(node.left)
            print(node.value, end=' ')
            self.search(node.right)

    def BFS(self, root):
        if not root:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs_preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.dfs_preorder(node.left)
            self.dfs_preorder(node.right)

    def dfs_inorder(self, node):
        if node:
            self.dfs_inorder(node.left)
            print(node.value, end=' ')
            self.dfs_inorder(node.right)

    def dfs_postorder(self, node):
        if node:
            self.dfs_postorder(node.left)
            self.dfs_postorder(node.right)
            print(node.value, end=' ')

class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        x.right = T2
        y.left = z
        z.height = max(height(z.left), height(z.right)) + 1
        y.height = max(height(y.left), height(y.right)) + 1
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(height(y.left), height(y.right)) + 1
        x.height = max(height(x.left), height(x.right)) + 1
        return y

    def rebalance(self, node):
       if not node:
           return 0
       return node.height

bt = BinaryTree()
values = [3, 10, 12, 0, 3, 2, 7]
for value in values:
    bt.insert(value)

avl = AVLTree()
avl_values = [3, 10, 12, 0, 3, 2, 7]
for value in avl_values:
    avl.insert(value)


bt.search(bt.root)
print('')
avl.BFS(bt.root)
print('')
avl.dfs_preorder(bt.root)
print('')
avl.dfs_inorder(bt.root)
print('')
avl.dfs_postorder(bt.root)