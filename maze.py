maze_1 = dict()
maze_1["1, 1"] = ["1, 2", "2, 1"]
maze_1["2, 1"] = ["1, 1"]
maze_1["3, 1"] = ["3, 2"]
maze_1["1, 2"] = ["1, 1", "2, 2"]
maze_1["2, 2"] = ["1, 2"]
maze_1["3, 2"] = ["3, 1", "2, 2"]
maze_1["1, 3"] = ["1, 2"]
maze_1["2, 3"] = ["3, 3"]
maze_1["3, 3"] = ["2, 3"]


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

    while len(frontier) > 0:

        node = frontier.pop(0)
        print(node.position)

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
                # print(child_node)
                frontier.insert(0, Node(child_node, node))
                path_map[child_node] = node.position

    return "Nope"

print(maze_search(maze_1, "3, 1", "1, 3"))
