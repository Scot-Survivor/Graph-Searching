import random


class Node:
    def __init__(self, value: str | int, cost: int, heuristic: int, goal: bool = False):
        self.cost: int = cost
        self.heuristic: int = heuristic
        self.value: str | int = value
        self.goal = goal
        self.right: Node | None = None
        self.left: Node | None = None


class Graph:
    def __init__(self):
        self.nodes: list[Node] = []
        self.vists = {
            'bfs': 0,
            'dfs': 0,
            'greedy': 0,
            'a_star': 0,
            'uniform': 0
        }
        self.stop_depth = False

    def breadth_first(self):
        queue = [self.nodes[0]]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value, end=" ")
            self.vists['bfs'] += 1
            if node.goal:
                return
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()

    def depth_first(self):

        def traverse_pre_order(node: Node):
            if node is None or self.stop_depth:
                return
            print(node.value, end=" ")
            self.vists['dfs'] += 1
            if node.goal:
                self.stop_depth = True
                return
            traverse_pre_order(node.left)
            traverse_pre_order(node.right)

        if self.nodes:
            traverse_pre_order(self.nodes[0])
            print()

    def greedy(self):
        """
        Greedy algorithm
        :return:
        """
        def greedy_search(node):
            if node is None:
                return
            print(node.value, end=" ")
            self.vists['greedy'] += 1
            if node.goal:
                return

            # If both children exist, choose the one with the lower heuristic value
            if node.left is not None and node.right is not None:
                if node.left.heuristic < node.right.heuristic:
                    greedy_search(node.left)
                else:
                    greedy_search(node.right)
            elif node.left is not None:
                greedy_search(node.left)
            elif node.right is not None:
                greedy_search(node.right)

        if self.nodes:
            greedy_search(self.nodes[0])
            print()

    def uniform(self):
        """
        Uniform search algorithm
        :return:
        """
        def uniform_search(node):
            if node is None:
                return
            print(node.value, end=" ")
            self.vists['uniform'] += 1
            if node.goal:
                return

            # If both children exist, choose the one with the lower heuristic value
            if node.left is not None and node.right is not None:
                if node.left.cost < node.right.cost:
                    uniform_search(node.left)
                else:
                    uniform_search(node.right)
            elif node.left is not None:
                uniform_search(node.left)
            elif node.right is not None:
                uniform_search(node.right)

        if self.nodes:
            uniform_search(self.nodes[0])
            print()

    def a_star(self):
        """
        A* algorithm
        :return:
        """

        def a_star_search(node):
            if node is None:
                return

            print(node.value, end=" ")
            self.vists['a_star'] += 1

            if node.goal:
                return

            if node.left is not None and node.right is not None:
                # Compare heuristics and choose the node with the lower heuristic value
                if node.left.heuristic < node.right.heuristic:
                    a_star_search(node.left)
                    a_star_search(node.right)
                else:
                    a_star_search(node.right)
                    a_star_search(node.left)
            elif node.left is not None:
                # Only left child exists
                a_star_search(node.left)
            elif node.right is not None:
                # Only right child exists
                a_star_search(node.right)

        if self.nodes:
            a_star_search(self.nodes[0])
            print()

    def display_graph(self):
        if not self.nodes:
            return

        root = self.nodes[0]
        max_level = self._height(root)
        lines, *_ = self._display_aux(root)
        for line in lines:
            print(line)

    @staticmethod
    def _get_line(node: Node):
        string = f"{node.value}(T)" if node.goal else f"{node.value}"
        string += f"(C: {node.cost},H: {node.heuristic})"
        return string

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = self._get_line(node)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = self._get_line(node)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = self._get_line(node)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = self._get_line(node)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def _height(self, node: Node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def get_height(self):
        return self._height(self.nodes[0])

    def get_visits(self, algo: str):
        return self.vists[algo]


def generate_random_graph_connected(nodes: int, max_cost: int, max_heuristic: int, goals: int = 1) -> Graph:
    graph = Graph()
    if nodes == 0:
        return graph

    # Create the first node
    graph.nodes.append(Node(1, 0, 0))

    for i in range(1, nodes):
        value = 1+i
        new_node = Node(value, random.randint(1, max_cost), random.randint(1, max_heuristic))

        # Try to connect the new node to existing nodes
        connected = False
        while not connected:
            parent = graph.nodes[random.randint(0, len(graph.nodes) - 1)]
            if parent.left is None:
                parent.left = new_node
                connected = True
            elif parent.right is None:
                parent.right = new_node
                connected = True
            else:
                # If both left and right are occupied, connect to another node
                random_node = graph.nodes[random.randint(0, len(graph.nodes) - 1)]
                if random_node.left is None:
                    random_node.left = new_node
                    connected = True
                elif random_node.right is None:
                    random_node.right = new_node
                    connected = True

        graph.nodes.append(new_node)

    # Select goals
    for _ in range(goals):
        goal = None
        while goal is None or goal.goal or goal == graph.nodes[0]:
            goal = graph.nodes[random.randint(0, nodes - 1)]
        goal.goal = True
    return graph
