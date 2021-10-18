wall_dict = {
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15,
}

dir_dict = {
    # down
    0:[0, 1],
    # left
    1:[-1, 0],
    # top
    2:[0, -1],
    # right
    3:[1, 0],
}

def get_walls(s):
    n = int(s) if s.isnumeric() else wall_dict[s]
    return [v for k, v in dir_dict.items() if 0 == n >> k & 1]

def init_graph(width, height, data):
    graph = {}
    for w in range(width):
        for h in range(height):
            graph[w, h] = []
            walls = get_walls(data[h][w])
            for a in walls:
                tw = w + a[0]
                th = h + a[1]
                graph[w, h].append((tw, th))
    return graph

def BFS(graph, start, rabbit):
    queue = []
    paths = []
    queue.append([start])
    seen = set()
    seen.add(start)

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == rabbit:
            paths.append(path)

        for n in graph[node]:
            if n in seen:
                continue

            new_path = list(path)
            new_path.append(n)
            queue.append(new_path)

    return paths

m = [
    'e65c',
    'abea',
    '2519',
    '355d',
]
graph = init_graph(4, 4, m)
print(BFS(graph, (0,0), (1, 1)))