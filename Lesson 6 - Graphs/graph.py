class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        self.nodes.append(Node(new_node_val))

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found, to_found = None, None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        return [(edge.value, edge.node_from.value, edge.node_to.value)
                for edge in self.edges]

    def get_adjacency_dict(self):
        adjancency_dict = {}
        for edge in self.edges:
            if not edge.node_from.value in adjancency_dict:
                adjancency_dict[edge.node_from.value] = []
            adjancency_dict[edge.node_from.value].append(
                (edge.node_to.value, edge.value))
        return adjancency_dict

    def get_adjacency_list(self):
        adjacency_dict = self.get_adjacency_dict()
        max_node_value = max([node.value for node in self.nodes])

        return [adjacency_dict.get(x) for x in range(max_node_value+1)]

    def get_adjacency_matrix(self):
        adjacency_dict = self.get_adjacency_dict()
        max_node_value = max([node.value for node in self.nodes])
        adjacency_matrix = []

        for i in range(max_node_value+1):
            adjacency_matrix.append([])
            edges = dict(adjacency_dict.get(i, []))
            for j in range(max_node_value+1):
                adjacency_matrix[i].append(edges.get(j, 0))

        return adjacency_matrix

