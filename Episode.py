def init_graph(width, height, surface):
    def bomb_x_range(cur, end, step, h, ret):
        t = cur + step
        if t < 0 or t >= width:
            return
        if surface[(t, h)] == '#' or t == end:
            return
        ret.append((t, h))
        bomb_x_range(t, end, step, h, ret)

    def bomb_y_range(cur, end, step, w, ret):
        t = cur + step
        if t < 0 or t >= height:
            return
        if surface[(w, t)] == '#' or t == end:
            return
        ret.append((w, t))
        bomb_y_range(t, end, step, w, ret)

    graph = {}
    for w in range(width):
        for h in range(height):
            if surface[w, h] == '#':
                continue
            t = []
            bomb_x_range(w, w+4, 1, h, t)
            bomb_x_range(w, w-4, -1, h, t)
            bomb_y_range(h, h+4, 1, w, t)
            bomb_y_range(h, h-4, -1, w, t)
            bomb_count = sum(1 for tt in t if surface[tt] == '@')
            if bomb_count > 0:
                graph[(w, h)] = t

    return graph

def reset_surveillance(surface):
    return sum(1 for k,v in surface.items() if v=='@')

def place_bomb(graph, surface, bombs):
    bombs_count = {k: sum(1 for t in v if surface[t] == '@') for k, v in graph.items() if surface[k] != '@'}
    max_info = ['', 0]
    for k, v in bombs_count.items():
        if v > max_info[1]:
            max_info[0] = k
            max_info[1] = v
    if bombs == 1 and max_info[1] < reset_surveillance(surface):
        print('WAIT')
        return True
    if max_info[1] == 0:
        print('WAIT')
        return True
    else:
        for k in graph[max_info[0]]:
            surface[k] = '.'

        del graph[max_info[0]]
        print(max_info[0][0], max_info[0][1])
        return False

surface_data = ['........', '......@.', '@@@.@@@@', '......@.', '........', '........']
width = len(surface_data[0])
height = len(surface_data)
surface = {}
for w in range(width):
    for h in range(height):
        surface[w,h] = surface_data[h][w]

graph = init_graph(width, height, surface)

bombs = 2
rounds = 10

while 1:
    if rounds == 0:
        break
    ret = place_bomb(graph, surface, bombs)
    if not False:
        bombs -= 1
    rounds -= 1
    # print(ret)
    # if ret:
    #     break