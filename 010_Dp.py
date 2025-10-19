# 01
# Реализуйте функцию, решающую задачу о рюкзаке с помощью
# динамического программирования. Вам дан рюкзак с
# определенной вместимостью и набор предметов с заданными
# весами и стоимостями. Необходимо найти максимальную
# стоимость предметов, которые можно поместить в рюкзак

# def knapsack(weights, values, capacity):
#     n = len(weights)
#     dp = [[0] * (capacity + 1) for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#
#     return dp[n][capacity]
#
#
# weights = [1, 2, 3, 4]
# values = [60, 100, 120, 10]
# capacity = 5
# print(knapsack(weights, values, capacity))


# 02
# Реализуйте функцию, которая находит длину наибольшей общей
# подпоследовательности (LCS) двух строк

# def lcs(a, b):
#     len_a = len(a)
#     len_b = len(b)
#
#     dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
#     for i in range(1, len_a + 1):
#         for j in range(1, len_b + 1):
#             if a[i - 1] == b[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#     return dp[len_a][len_b]
#
#
# a = 'abcdefjhigkl'
# b = 'acejikm'
# print(lcs(a, b))


# 03
# Реализуйте функцию, которая находит количество способов
# разбить число n на сумму чисел, используя динамическое
# программирование

# def number_of_partitions(num):
#     dp = [0] * (num + 1)
#     dp[0] = 1
#
#     for i in range(1, num + 1):
#         for j in range(i, num + 1):
#             dp[j] += dp[j - i]
#
#     return dp[num]
#
# num = 6
# print(number_of_partitions(num))


# 04
# Реализуйте алгоритм Флойда-Уоршелла для нахождения
# кратчайших путей между всеми парами вершин в графе,
# представленного в виде матрицы смежности

def shortest_part(graph, start = 0):
    n = len((graph))
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = min((dist[v], v) for v in range(n) if not visited[v])[1]
        visited[u] = True

        for v in range(n):
            if graph[u][v] > 0  and not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    return dist

graph = [
    [0, 1, 2, 3],
    [1, 1, 1, 3],
    [4, 0, 3, 5],
    [1, 0, 0, 3]
]

print(shortest_part(graph))