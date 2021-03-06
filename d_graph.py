# Course: CS261 - Data Structures
# Author: Mark Mendez
# Assignment: 6
# Description: Implements a class for creating, manipulating, and querying a directed graph

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a new unnamed vertex to the graph
        First vertex created in the graph will be assigned index 0, subsequent vertices will have indexes 1, 2, 3 etc.
        :return: int showing the number of vertices in the graph, including the new one
        """
        # handle adding first vertex
        if self.v_count == 0:
            self.adj_matrix.append([0])
            self.v_count += 1
            return self.v_count

        # label each existing vertex as not connected to the new one
        for neighbor_group in self.adj_matrix:
            neighbor_group.append(0)

        # add the new vertex
        new_length = len(self.adj_matrix[0])
        new_list = [0 for index in range(new_length)]
        self.adj_matrix.append(new_list)

        # update member variable counting vertices
        self.v_count += 1

        return self.v_count

    def vertices_are_valid(self, src: int, dst: int) -> bool:
        """
        Validates two vertices
        :param src: int identifying a vertex
        :param dst: int identifying a different vertex
        :return: True if the vertices are valid; False otherwise
        """
        # check for out-of-bounds indices
        if src >= self.v_count or dst >= self.v_count or src < 0 or dst < 0:
            return False

        # check for same indices
        if src == dst:
            return False

        # passed tests; vertices are valid
        return True

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds a new edge to the graph, connecting two vertices with provided indices
        If a vertex index does not exist in the graph
            or the weight is not a positive integer
            or src and dst are the same vertex,
            nothing happens
        If an edge already exists in the graph, its weight will be updated
        :param src: int identifying the vertex to which the edge will be added
        :param dst: int identifying the vertex which will be added to src as the new edge
        :param weight: (optional) int representing the weight of the new edge. If not provided, it is 1
        """
        if not self.vertices_are_valid(src, dst):
            return

        # check for invalid weight
        if weight < 1:
            return

        # update src -> dst weight
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between two vertices with provided indices
        If an index does not exist in the graph
            or if there is no edge between them
            or if src and dst are the same vertex,
            nothing happens
        :param src: int identifying the vertex from which the edge will be removed
        :param dst: int identifying the vertex which will be removed from src as the edge
        """
        if not self.vertices_are_valid(src, dst):
            return

        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        pass

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        pass

    def has_cycle(self):
        """
        TODO: Write this implementation
        try https://www.baeldung.com/cs/detecting-cycles-in-directed-graph
        """
        pass

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)
    #
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)

    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    print(g)
    for edge in edges:
        src, dst, weight = edge
        g.remove_edge(src, dst)
        print('after removing', src, '->', dst, '\n', g)


    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    # for path in test_cases:
    #     print(path, g.is_valid_path(path))
    #
    #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    #
    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    #
    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)
    #
    #
    # print("\nPDF - dijkstra() example 1")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    # g.remove_edge(4, 3)
    # print('\n', g)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
