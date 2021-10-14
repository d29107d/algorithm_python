def init_graph(width, height, surface):
    graph = {}
    add = [-1, 1]
    for w in range(width):
        for h in range(height):
            graph[w, h] = []
            if surface[w, h] == '#':
                continue
            for a in add:
                tw = w + a
                th = h + a
                if tw >= 0 and tw < width and surface[(tw, h)] == 'O':
                    graph[w, h].append((tw, h))
                if th >= 0 and th < height and surface[(w, th)] == 'O':
                    graph[w, h].append((w, th))
    return graph

def BFS(graph, start, surface):
    if surface[start] == '#': return 0

    queue = [start]
    seen = set(start)
    count = -1
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        count += 1

    return count if count > 0 else 1

surface_data = []
with open('surface.txt') as file:
    lines = file.readlines()
    surface_data = [line.strip() for line in lines]

width, height = len(surface_data[0]), len(surface_data)
surface = {}
for w in range(width):
    for h in range(height):
        surface[w,h] = surface_data[h][w]
# print(surface)
graph = init_graph(width, height, surface)
print(BFS(graph, (520,960), surface))