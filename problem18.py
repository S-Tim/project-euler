input_text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


class Node:
    node_id = 0

    def __init__(self, value):
        self.id = Node.node_id
        Node.node_id += 1
        self.value = value
        self.children = []
        self.previous = None

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f'{self.id}: value={self.value}, children={list(map(lambda node: node.id, self.children))}, previous={self.previous.id if self.previous is not None else "None"}'


def read_graph(graph_text: str):
    graph = []
    values = [list(map(lambda value: Node(100 - int(value)), line.split())) for line in graph_text.splitlines()]
    for i in range(len(values)):
        for j in range(len(values[i])):
            current_node = values[i][j]
            if i < len(values) - 1:
                current_node.add_child(values[i + 1][j])
                current_node.add_child(values[i + 1][j + 1])
            graph.append(current_node)

    return graph


def dijkstra(graph, start_node):
    # stores the visited nodes with the minimal distance to them
    unvisited = {node: 10000 for node in graph}
    visited = {}
    current_node = start_node
    unvisited[current_node] = current_node.value

    while len(unvisited) > 0:
        for child in current_node.children:
            if child in unvisited:
                new_distance = unvisited[current_node] + child.value
                if new_distance < unvisited[child]:
                    unvisited[child] = new_distance
                    child.previous = current_node

        visited[current_node] = unvisited[current_node]
        unvisited.pop(current_node)

        # print(visited)
        # print(unvisited)
        if len(unvisited) > 0:
            k, v = sorted(unvisited.items(), key=lambda item: item[1])[0]
            current_node = k
            # current_node = list(filter(lambda node: node.id == k, graph))[0]

    return visited


# select non-visited node with least distance
# remove this node from the list
# look at all the neighbors and see if you can reach them faster than before
def main():
    graph = read_graph(input_text)
    # print(len(graph))
    # print(graph)
    distances = dijkstra(graph, graph[0])
    # print(distances)

    goals = []
    for node in graph[-15:]:
        goals.append((node, distances[node]))

    highest = list(sorted(goals, key=lambda node: node[1]))[0]

    # highest = list(sorted(distances.items(), key=lambda node: node[1]))[0]
    print(highest)

    highest_node = highest[0]
    sum = 0
    while highest_node.previous is not None:
        print(100 - highest_node.value)
        sum += 100 - highest_node.value
        highest_node = highest_node.previous
    print(100 - highest_node.value)
    print(sum + 100 - highest_node.value)


if __name__ == '__main__':
    main()
