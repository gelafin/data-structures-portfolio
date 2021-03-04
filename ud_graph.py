# Course: CS 261
# Author: Mark Mendez
# Assignment: 6
# Description: Implements a class for creating, manipulating, and querying an undirected graph


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def is_in_graph(self, vertex: str) -> bool:
        """
        Checks whether a vertex is in the graph
        :param vertex: string indicating the vertex to check
        :return: True if the vertex is in the graph; False otherwise
        """
        try:
            # test by trying to access the vertex
            copy = self.adj_list[vertex]
        except KeyError:
            return False

        # passed the test; it's in the graph
        return True

    def are_connected(self, vertex_1: str, vertex_2: str) -> bool:
        """
        Checks whether two vertices are connected by an edge
        Vertices must be valid and different
        :param vertex_1: string identifying a valid vertex
        :param vertex_2: string identifying a different valid vertex
        :return: True if the vertices are connected; False otherwise
        """
        if vertex_1 in self.adj_list[vertex_2]:  # no need to test both directions, since it's an undirected graph
            # passed the test; vertices are connected
            return True

        # failed the test; vertices are not connected
        return False

    def add_vertex(self, vertex: str) -> None:
        """
        Adds a new vertex to the graph
        Duplicates are silently rejected
        :param vertex: string to add as a new vertex. Vertices can be any string
        """
        # silently reject duplicates
        if self.is_in_graph(vertex):
            return

        # add the new vertex string as a key in the adj_list
        self.adj_list[vertex] = []

    def add_edge(self, vertex_1: str, vertex_2: str) -> None:
        """
        Adds a new edge to the graph, connecting two vertices with the provided names
        If a vertex does not exist in the graph, it will be created, then the edge will be added
        If the edge already exists or both params refer to the same vertex, nothing happens
        :param vertex_1: string identifying a vertex
        :param vertex_2: string identifying a vertex to connect to vertex_1
        """
        # if the vertices are the same, do nothing
        if vertex_1 == vertex_2:
            return

        # if a vertex is not in the graph yet, add it
        if not self.is_in_graph(vertex_1):
            self.add_vertex(vertex_1)
        if not self.is_in_graph(vertex_2):
            self.add_vertex(vertex_2)

        # if the edge already exists, do nothing
        if self.are_connected(vertex_1, vertex_2):
            return

        # mutually connect vertices by adding them to each other's list
        self.adj_list[vertex_1].append(vertex_2)
        self.adj_list[vertex_2].append(vertex_1)

    def remove_edge(self, vertex_1: str, vertex_2: str) -> None:
        """
        Removes an edge from the graph
        If a vertex name does not exist in the graph, or if there is no edge between them, nothing happens
        :param vertex_1: string identifying a vertex
        :param vertex_2: string identifying a vertex connected to vertex_1 whose edge will be removed
        """
        # make sure the vertices are in the graph
        if not self.is_in_graph(vertex_1) or not self.is_in_graph(vertex_2):
            return

        # make sure the vertices are connected by an edge
        if not self.are_connected(vertex_1, vertex_2):
            return

        # remove the edge by removing vertices from each other's list
        self.adj_list[vertex_1].remove(vertex_2)
        self.adj_list[vertex_2].remove(vertex_1)

    def remove_vertex(self, vertex: str) -> None:
        """
        Removes a vertex and all connected edges
        If the vertex does not exist in the graph, nothing happens
        :param vertex: string identifying a vertex
        """
        # make sure the vertex is in the graph
        if not self.is_in_graph(vertex):
            return

        # remove the vertex
        del self.adj_list[vertex]

        # remove the old vertex's edges
        for existing_vertex in self.adj_list:
            # note that 'try...remove()' is more efficient than 'in...remove()'
            try:
                self.adj_list[existing_vertex].remove(vertex)
            except ValueError:
                # nothing to remove
                pass

    def get_vertices(self) -> []:
        """
        Returns a list of vertices in the graph (not in any order)
        """
        return self.adj_list.keys()

    def get_edges(self) -> []:
        """
        Returns a list of edges in the graph (not in any order)
        :return: list of edges, where an edge is a tuple of two strings identifying incident vertices
        """
        

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
       

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
       

    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        

    def count_connected_components(self):
        """
        Return number of connected componets in the graph
        """
      

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
       

   


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = UndirectedGraph()
    # print(g)
    #
    # for v in 'ABCDE':
    #     g.add_vertex(v)
    # print(g)
    #
    # g.add_vertex('A')
    # print(g)
    #
    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)


    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)
    #
    #
    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')
    #
    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    # for path in test_cases:
    #     print(list(path), g.is_valid_path(list(path)))
    #
    #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = 'ABCDEGH'
    # for case in test_cases:
    #     print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    # print('-----')
    # for i in range(1, len(test_cases)):
    #     v1, v2 = test_cases[i], test_cases[-1 - i]
    #     print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')
    #
    #
    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    #     'add FG', 'remove GE')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print('{:<10}'.format(case), g.has_cycle())
