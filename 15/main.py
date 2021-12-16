import functools
import math

def get_min(queue, dist):
    min_dist = math.inf
    ret = None
    for i in queue:
        if dist[i] < min_dist:
            min_dist = dist[i]
            ret = i
    return ret


def part1(graph):
    node_queue = []
    dist = {}
    vals = {}
    for i in range(len(graph)):
        for j in range(len(graph)):
            node_queue.append(graph[i][j])
            dist[graph[i][j]] = math.inf
            vals[graph[i][j]] = graph[i][j].val
    dist[graph[0][0]] = 0

    while len(node_queue) > 0:
        u = get_min(node_queue, dist)
        node_queue.remove(u)

        for v in u.neighbors:
            alt = dist[u] + vals[v]
            if alt < dist[v]:
                dist[v] = alt
    print(dist[graph[len(graph)-1][len(graph)-1]])


def part2(graph):
    node_queue = []
    node_lookup = []

    dist = {}
    vals = {}
    for i in range(len(graph)):
        for j in range(len(graph)):
            node_queue.append(graph[i][j])
            dist[graph[i][j]] = math.inf
            vals[graph[i][j]] = graph[i][j].val
    dist[graph[0][0]] = 0
    node_lookup.append(graph[0][0])

    while len(node_queue) > 0:
        u = functools.reduce(lambda a, b: a if dist[a] < dist[b] else b, node_lookup)
        node_queue.remove(u)
        node_lookup.remove(u)

        for v in u.neighbors:
            alt = dist[u] + vals[v]
            if alt < dist[v]:
                node_lookup.append(v)
                dist[v] = alt

    print(dist[graph[len(graph)-1][len(graph)-1]])


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)


matrix = []
matrix2 = []
lines = open("input.txt", "r").readlines()

for line in lines:
    matrix.append([Node(int(line[i])) for i in range(0, len(line.rstrip()))])

for i in range(0, len(lines)*5):
    matrix2.append([0 for j in range(len(lines) * 5)])

for i in range(0, len(lines) * 5):
    for j in range(0, len(lines) * 5):
        line = lines[i % len(lines)].rstrip()
        matrix2[i][j] = Node(int(line[j % len(lines)]) + int(i / len(lines)) + int(j / len(lines)))
        if matrix2[i][j].val > 9:
            matrix2[i][j].val %= 9

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        if i != 0:
            matrix[i][j].add_neighbor(matrix[i-1][j])
        if j != 0:
            matrix[i][j].add_neighbor(matrix[i][j-1])
        if i != len(matrix)-1:
            matrix[i][j].add_neighbor(matrix[i + 1][j])
        if j != len(matrix)-1:
            matrix[i][j].add_neighbor(matrix[i][j + 1])

for i in range(0, len(matrix2)):
    for j in range(0, len(matrix2)):
        if i != 0:
            matrix2[i][j].add_neighbor(matrix2[i-1][j])
        if j != 0:
            matrix2[i][j].add_neighbor(matrix2[i][j-1])
        if i != len(matrix2)-1:
            matrix2[i][j].add_neighbor(matrix2[i + 1][j])
        if j != len(matrix2)-1:
            matrix2[i][j].add_neighbor(matrix2[i][j + 1])

part2(matrix2)