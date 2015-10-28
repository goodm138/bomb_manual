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
                path.insert(0, current)
                if current in path_map:
                    current = path_map[current]
                else:
                    break
            return path

        explored_set.append(node.position)

        child_nodes = maze[node.position]

        for child_node in child_nodes:
            if child_node not in explored_set:
                frontier.append(Node(child_node, node))
                path_map[child_node] = node.position

    return None


def print_path(path):
    if path is None:
        print("Error occurred, try again")
        return

    direction = ""
    route = list()

    print("")

    for i in range(0, len(path) - 1, 1):

        if int(path[i + 1][0]) > int(path[i][0]):
            direction = "Right"
        if int(path[i + 1][0]) < int(path[i][0]):
            direction = "Left"
        if int(path[i + 1][3]) > int(path[i][3]):
            direction = "Up"
        if int(path[i + 1][3]) < int(path[i][3]):
            direction = "Down"

        route.append(direction)

    dir_count = 1
    for i in range(0, len(route) - 1, 1):
        if route[i] == route[i + 1]:
            dir_count += 1
        else:
            print(route[i], dir_count)
            print("")
            dir_count = 1

    print(route[len(route) - 1], dir_count)
    print("")


def get_maze(marker_1, marker_2):
    maze = dict()

    maze_1 = ["1, 5", "6, 4"]

    if marker_1 in maze_1 and marker_2 in maze_1:
        maze["1, 1"] = ["1, 2", "2, 1"]
        maze["2, 1"] = ["1, 1"]
        maze["3, 1"] = ["3, 2", "4, 1"]
        maze["4, 1"] = ["3, 1", "4, 2"]
        maze["5, 1"] = ["6, 1"]
        maze["6, 1"] = ["5, 1", "6, 2"]

        maze["1, 2"] = ["1, 1", "1, 3", "2, 2"]
        maze["2, 2"] = ["1, 2", "3, 2"]
        maze["3, 2"] = ["3, 1", "2, 2"]
        maze["4, 2"] = ["4, 1", "5, 2"]
        maze["5, 2"] = ["4, 2"]
        maze["6, 2"] = ["6, 1", "6, 3"]

        maze["1, 3"] = ["1, 2", "1, 4"]
        maze["2, 3"] = ["3, 3"]
        maze["3, 3"] = ["2, 3", "3, 4", "4, 3"]
        maze["4, 3"] = ["3, 3", "4, 4"]
        maze["5, 3"] = ["6, 3"]
        maze["6, 3"] = ["6, 2", "6, 4"]

        maze["1, 4"] = ["1, 3", "1, 5"]
        maze["2, 4"] = ["2, 5", "3, 4"]
        maze["3, 4"] = ["2, 4", "3, 3"]
        maze["4, 4"] = ["4, 3", "5, 4"]
        maze["5, 4"] = ["4, 4", "6, 4"]
        maze["6, 4"] = ["5, 4", "6, 3", "6, 5"]

        maze["1, 5"] = ["1, 4", "1, 6"]
        maze["2, 5"] = ["2, 4", "3, 5"]
        maze["3, 5"] = ["2, 5", "3, 6"]
        maze["4, 5"] = ["4, 6", "5, 5"]
        maze["5, 5"] = ["4, 5", "6, 5"]
        maze["6, 5"] = ["5, 5", "6, 4"]

        maze["1, 6"] = ["1, 5", "2, 6"]
        maze["2, 6"] = ["1, 6", "3, 6"]
        maze["3, 6"] = ["2, 6", "3, 5"]
        maze["4, 6"] = ["4, 5", "5, 6"]
        maze["5, 6"] = ["4, 6", "6, 6"]
        maze["6, 6"] = ["5, 6"]

    return maze
