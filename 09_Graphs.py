# 01
# Напишите класс DirectedGraph, который реализует
# ориентированный граф с методами добавления вершины
# (add_vertex) и добавления ребра (add_edge). Протестируйте
# реализацию на примере

# 02
# Напишите функцию для обхода ориентированного графа
# в ширину (Breadth-First Search, BFS)

from collections import deque

# class DirectedGraph:
#     def __init__(self): self.graph = {}
#
#     def add_vertex(self, v):
#         if v not in self.graph:
#             self.graph[v] = []
#
#     def add_edge(self, u, v):
#         self.add_vertex(u); self.add_vertex(v)
#         if v not in self.graph[u]:
#             self.graph[u].append(v)
#
#     def bfs(self, start):
#         if start not in self.graph: return []
#         vis, q, order = {start}, deque([start]), []
#         while q:
#             u = q.popleft(); order.append(u)
#             for w in self.graph[u]:
#                 if w not in vis:
#                     vis.add(w); q.append(w)
#         return order
#
#
# dg = DirectedGraph()
# vertex = ['A', 'B', 'C', 'D', 'E']
# for v in vertex:
#     dg.add_vertex(v)
#
# edge = [('A', 'B'), ('A', 'C'),
#         ('B', 'C'),
#         ('C', 'D'),
#         ('D', 'E'), ('D', 'B'),
#         ('E', 'A')
#         ]
# for from_v, to_v in edge:
#     dg.add_edge(from_v, to_v)
#
# print(dg.bfs('D'))

# 03
# Напишите функцию для создания матрицы смежности из
# списка ребер. Реализуйте функции для добавления вершины
# и ребра в граф, представленный в виде матрицы смежности

class Graph:
    def __init__(self, graphs):
        self.V = graphs
        self.graph = [[0] * graphs for _ in range(graphs)]
        self.vertex_map = {}
        self.vertices = []

    def add_vertex(self, vertex):
        if vertex not in self.vertex_map:
            index = len(self.vertices)
            self.vertex_map[vertex] = index
            self.vertices.append(vertex)

    def add_edge(self, from_v, to_v):
        from_index = self.vertex_map[from_v]
        to_index = self.vertex_map[to_v]
        self.graph[from_index][to_index] = 1

    def printed_graphs(self):
        for i, row in enumerate(self.graph):
            print(f'{self.vertices[i]} {row}')


edge = [('A', 'B'), ('A', 'C'),
        ('B', 'C'),
        ('C', 'D'),
        ('D', 'B')
        ]

all_verices = set()
for from_v, to_v in edge:
    all_verices.add(from_v)
    all_verices.add(to_v)

gr = Graph(len(all_verices))

for vertex in sorted(all_verices):
    gr.add_vertex(vertex)

for from_v, to_v in edge:
    gr.add_edge(from_v, to_v)

gr.printed_graphs()


# 04
# Напишите функции для создания списка смежности из списка
# ребер. Реализуйте функции для добавления вершины и ребра
# в граф, представленный в виде списка смежности

# class DirectedGraph:
#     def __init__(self):
#         self.graph = {}
#
#     def add_vertex(self, vertex):
#         if vertex not in self.graph:
#             self.graph[vertex] = []
#             print(f'Добавлена вершина {vertex}')
#         else:
#             print(f'{vertex} -  уже существует')
#
#     def add_edge(self, from_v, to_v):
#         if to_v not in self.graph[from_v]:
#             self.graph[from_v].append(to_v)
#             print(f'Добавлено ребро {from_v} - {to_v}')
#         else:
#             print(f'Ребро {from_v} - {to_v} уже существует')
#
#     def printed_graph(self):
#         for node in self.graph:
#             print(f'{node} - {self.graph[node]}')
#
# dg = DirectedGraph()
# vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'I']
# for v in vertex:
#     dg.add_vertex(v)
#
# edge = [('A', 'B'), ('A', 'C'),
#         ('B', 'C'),
#         ('C', 'D'),
#         ('D', 'E'), ('D', 'B'),
#         ('E', 'A'), ('E', 'F'),
#         ('F', 'I')
#         ]
# for from_v, to_v in edge:
#     dg.add_edge(from_v, to_v)
#
# dg.printed_graph()