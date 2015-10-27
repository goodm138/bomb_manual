maze_1 = dict()

maze_1["1, 1"] = ["1, 2", "2, 1"]
maze_1["2, 1"] = ["1, 1"]
maze_1["3, 1"] = ["3, 2", "4, 1"]
maze_1["4, 1"] = ["3, 1", "4, 2"]
maze_1["5, 1"] = ["6, 1"]
maze_1["6, 1"] = ["5, 1", "6, 2"]

maze_1["1, 2"] = ["1, 1", "1, 3", "2, 2"]
maze_1["2, 2"] = ["1, 2", "3, 2"]
maze_1["3, 2"] = ["3, 1", "2, 2"]
maze_1["4, 2"] = ["4, 1", "5, 2"]
maze_1["5, 2"] = ["4, 2"]
maze_1["6, 2"] = ["6, 1", "6, 3"]

maze_1["1, 3"] = ["1, 2", "1, 4"]
maze_1["2, 3"] = ["3, 3"]
maze_1["3, 3"] = ["2, 3", "3, 4", "4, 3"]
maze_1["4, 3"] = ["3, 3", "4, 4"]
maze_1["5, 3"] = ["6, 3"]
maze_1["6, 3"] = ["6, 2", "6, 4"]

maze_1["1, 4"] = ["1, 3", "1, 5"]
maze_1["2, 4"] = ["2, 5", "3, 4"]
maze_1["3, 4"] = ["2, 4", "3, 3"]
maze_1["4, 4"] = ["4, 3", "5, 4"]
maze_1["5, 4"] = ["4, 4", "6, 4"]
maze_1["6, 4"] = ["5, 4", "6, 3", "6, 5"]

maze_1["1, 5"] = ["1, 4", "1, 6"]
maze_1["2, 5"] = ["2, 4", "3, 5"]
maze_1["3, 5"] = ["2, 5", "3, 6"]
maze_1["4, 5"] = ["4, 6", "5, 5"]
maze_1["5, 5"] = ["4, 5", "6, 5"]
maze_1["6, 5"] = ["5, 5", "6, 4"]

maze_1["1, 6"] = ["1, 5", "2, 6"]
maze_1["2, 6"] = ["1, 6", "3, 6"]
maze_1["3, 6"] = ["2, 6", "3, 5"]
maze_1["4, 6"] = ["4, 5", "5, 6"]
maze_1["5, 6"] = ["4, 6", "6, 6"]
maze_1["6, 6"] = ["5, 6"]


class Node:

    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent


def maze_search(maze, start, end):

    node = Node(start)

    frontier = list()
    frontier.append(node)

    explored_set = list()

    path_map = dict()
    path = list()

    while len(frontier) > 0:

        node = frontier.pop(0)

        if node.position == end:
            current = end
            while current is not None:
                print(current)
                if current in path_map:
                    current = path_map[current]
                else:
                    break
            return "Done"

        explored_set.append(node.position)

        child_nodes = maze[node.position]

        for child_node in child_nodes:
            if child_node not in explored_set:
                frontier.append(Node(child_node, node))
                path_map[child_node] = node.position

    return "Nope"

print(maze_search(maze_1, "2, 1", "6, 6"))
