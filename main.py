from graphviz import Digraph
from graph import generate_random_graph_connected, Graph, Node


def generate_graphviz(graph: Graph, filename: str = "graphviz_output"):
    dot = Digraph()

    def traverse_and_add_edges(node: Node, parent_id=None):
        if node is None:
            return
        dot.node(str(node.value), label=graph._get_line(node), color='red' if node.goal else 'black')
        if parent_id is not None:
            dot.edge(str(parent_id), str(node.value))
        if node.left:
            traverse_and_add_edges(node.left, node.value)
        if node.right:
            traverse_and_add_edges(node.right, node.value)

    if graph.nodes:
        traverse_and_add_edges(graph.nodes[0])

    # Set rank to same for nodes at the same level
    dot.attr(rank='same')
    dot.render(filename, format='png', cleanup=True)


if __name__ == '__main__':
    nodes = int(input("Enter number of nodes: ").strip() or "10")
    max_cost = int(input("Enter max cost: ").strip() or "11")
    max_heuristic = int(input("Enter max heuristic: ").strip() or "11")
    max_goals = int(input("Enter number of goals: ").strip() or "1")
    graph = generate_random_graph_connected(nodes, max_cost, max_heuristic, max_goals)
    g_height = graph.get_height()
    print(g_height*5 * ' ' + "GRAPH")
    graph.display_graph()
    print("_" * g_height*10)
    print("Breadth First")
    graph.breadth_first()
    print("\nDepth First")
    graph.depth_first()
    print("Greedy")
    graph.greedy()
    print("A Star")
    graph.a_star()
    print("Uniform")
    graph.uniform()

    print("\n" * 3 + "BFS Visits: ", graph.get_visits('bfs'))
    print("DFS Visits: ", graph.get_visits('dfs'))
    print("Greedy Visits: ", graph.get_visits('greedy'))
    print("A* Visits: ", graph.get_visits('a_star'))
    print("Uniform Visits: ", graph.get_visits('uniform'))
    print("\n"*3)
    print("Number of Nodes: ", len(graph.nodes))
    print("Number of Goals: ", len(list(filter(lambda x: x.goal, graph.nodes))))
    print("\n")
    print("Goal List: " + ", ".join([str(node.value) for node in filter(lambda x: x.goal, graph.nodes)]))
    try:
        generate_graphviz(graph, "graphviz_output")
    except Exception as e:
        print("Error generating graphviz: ", e)
        print("Please install graphviz and add it to your PATH.")
