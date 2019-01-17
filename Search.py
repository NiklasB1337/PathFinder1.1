
from queue import Queue, PriorityQueue

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

class Graph():

    def neighbors(node):
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if 0 <= neighbor[0] < 20 and 0 <= neighbor[1] < 10:
                result.append(neighbor)
                return result

    # Astar
    def astar(self, maze, start, end):

        """Returns a list of tuples as a path from the given start to the given end in the given maze"""

        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until the end is found
        while len(open_list) > 0:

            # get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # finding the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path

            # generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

                # get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # make sure the node is within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                        len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                    continue

                # make sure the terrain is walkable
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # loop through children
            for child in children:

                # child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                #cCreate the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                            (child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # add the child to the open list
                open_list.append(child)

    # Dijkstra
    def dijkstra(self, maze, start, end):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == end:
                break

            for next in maze.neighbors(current):
                new_cost = cost_so_far[current] + maze.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put(next, priority)
                    came_from[next] = current

    # breadth first
    def bfsearch(self, maze, start, end):
        frontier = Queue()
        frontier.put(start)

        came_from = {start: True}

        while not frontier.empty():
            current = frontier.get()

            #Early exit
            if current == end:
                break

            print('Visiting {}'.format(current))
            for next in maze.neighbors(current):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = True

        return came_from
