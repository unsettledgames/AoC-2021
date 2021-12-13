import copy


def part1(graph):
    print(DFS(graph, [], 'start'))


def part2(graph):
    spaths = []
    ret = DFS2(graph, [], 'start', '', [], spaths)
    out = open("out.txt", "w")
    out.writelines([",".join(path)+"\n" for path in spaths])

    print(len(set("".join(path) for path in spaths)))


def DFS2(graph, visited, curr, small, curr_path, spaths):
    ret = 0
    curr_path.append(curr)
    visited += [curr]

    if curr == 'end':
        spaths.append(curr_path)
        return 1
    else:
        neighbors = []
        new_small = small

        for path in graph:
            if path[0] == curr and (path[1] not in visited or path[1].upper() == path[1]):
                neighbors.append(path[1])
            elif path[0] == curr and path[1] == small:
                new_small = "0807"
                neighbors.append(path[1])
        for i in neighbors:
            if new_small == '' and new_small != '0807':
                for el in [path[1] for path in graph if path[1] != 'start' and path[1] != 'end' and path[1].upper() != path[1]]:
                    ret += DFS2(graph, copy.deepcopy(visited) + [i], i, el, copy.deepcopy(curr_path), spaths)
            ret += DFS2(graph, copy.deepcopy(visited) + [i], i, new_small, copy.deepcopy(curr_path), spaths)
    return ret


def DFS(graph, visited, curr):
    ret = 0
    visited += [curr]

    if curr == 'end':
        return 1
    else:
        neighbors = [path[1] for path in graph if path[0] == curr and (path[1] not in visited or path[1].upper() == path[1])]
        for i in neighbors:
            ret += DFS(graph, visited + [i], i)
    return ret


lines = open("input.txt", "r").readlines()
paths = []

for line in lines:
    nodes = line.split("-")
    nodes[0] = nodes[0].rstrip()
    nodes[1] = nodes[1].rstrip()

    paths.append(nodes)
    paths.append([nodes[1], nodes[0]])
part1(paths)
part2(paths)
