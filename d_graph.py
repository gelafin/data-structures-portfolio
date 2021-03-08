# Course: CS261 - Data Structures
# Author: Mark Mendez
# Assignment: 6
# Description: Implements a class for creating, manipulating, and querying a directed graph


from stack import Stack
from collections import deque
from heapq import *


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

    def vertices_are_valid(self, src: int, dst: int = None) -> bool:
        """
        Validates two vertices
        :param src: int identifying a vertex
        :param dst: int identifying a different vertex
        :return: True if the vertices are valid; False otherwise
        """
        # check for out-of-bounds src
        if src >= self.v_count or src < 0:
            return False

        if dst is not None:
            # check for out-of-bounds dst
            if dst >= self.v_count or dst < 0:
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
        Returns an unordered list of vertices in the graph
        :return: list of int vertices in the graph, unordered
        """
        return [vertex for vertex in range(len(self.adj_matrix))]

    def get_edges(self) -> []:
        """
        Returns an unordered list of edges in the graph
        Edges are tuples with the form (source, destination, weight), where:
            source is the source vertex
            destination is the destination vertex
            weight is the weight of the edge
        :return: list of edges in the graph, as unordered tuples of ints
        """
        # get all of the graph's vertices
        edges = []
        for outer_vertex in range(len(self.adj_matrix)):
            # get all of this source vertex's neighbors and their edge weights, adding each edge
            new_edges = self.get_direct_edges(outer_vertex)
            edges.extend(new_edges)

        return edges

    def get_direct_edges(self, vertex: int) -> list:
        """
        Returns an unordered list of edges connected to one vertex
        Edges are tuples with the form (source, destination, weight), where:
            source is the source vertex
            destination is the destination vertex
            weight is the weight of the edge
        :param vertex: int
        :return: list of edges in the graph, as unordered tuples of ints
        """
        edges = []
        neighbor_group = self.adj_matrix[vertex]

        # get all of this source vertex's neighbors and their edge weights, adding each edge
        for index in range(len(neighbor_group)):
            weight = self.adj_matrix[vertex][index]

            # if there is a weight, there is an edge; add it to the list
            if weight > 0:
                edge = (vertex, index, weight)
                edges.append(edge)

        return edges

    def get_children(self, vertex: int) -> list:
        """
        Returns a vertex's children
        :param vertex: int vertex whose children will be returned
        :return: list of ints identifying the given vertex's child vertices
        """
        return [child for child in range(len(self.adj_matrix[vertex])) if self.adj_matrix[vertex][child] > 0]

    def is_valid_path(self, path: []) -> bool:
        """
        Checks whether a given path is valid in the graph
        Empty paths are considered valid
        :param path: list of ints identifying vertices in the path
        :return: True if the path is valid; False otherwise
        """
        # handle empty path
        if len(path) == 0:
            return True

        # travel along the given path
        for index in range(len(path) - 1):  # -1 because loop reaches forward
            vertex = path[index]
            next_vertex = path[index + 1]

            # validate vertices
            if not self.vertices_are_valid(vertex, next_vertex):
                return False

            # check to make sure these vertices are connected by an edge
            if self.adj_matrix[vertex][next_vertex] < 1:
                return False

        # passed the above test, so path is valid
        return True

    def dfs(self, v_start: int, v_end: int = None) -> []:
        """
        Return list of vertices visited during DFS search, in visitation order
        Vertices are picked least to greatest
        If the starting vertex is not in the graph, returns an empty list
        :param v_start: int identifying the starting vertex
        :param v_end: (optional) int identifying the vertex after which to end the search early
                      if v_end is not in the graph, the whole graph is searched
        :return: list of ints identifying the visited vertices, or empty list if v_start isn't in the graph
        """
        # make sure v_start is in the graph
        if not self.vertices_are_valid(v_start):
            return []

        # make a set of visited vertices
        visited = set()
        visited.add(v_start)

        # make a stack of vertices to visit
        to_visit = Stack([v_start])

        # visit all direct successors in order
        vertex = v_start
        while not to_visit.is_empty() and vertex != v_end:
            # get a vertex to visit
            vertex = to_visit.pop()

            # mark this vertex as visited (if it hasn't been counted yet)
            if vertex not in visited:
                visited.add(vertex)

            # search unvisited direct successors for the next vertex
            successors_ordered = self.get_children(vertex)
            successors_ordered.sort(reverse=True)
            for potential_successor in successors_ordered:
                if potential_successor not in visited and self.adj_matrix[vertex][potential_successor] > 0:
                    # keep a trail of breadcrumbs for backtracking
                    to_visit.push(potential_successor)

        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        Returns a list of vertices visited during BFS search, in visitation order
        Vertices are picked least to greatest
        If the starting vertex is not in the graph, returns an empty list
        :param v_start: int identifying the starting vertex
        :param v_end: (optional) int identifying the vertex after which to end the search early
                      if v_end is not in the graph, the whole graph is searched
        :return: list of ints identifying the visited vertices, or empty list if v_start isn't in the graph
        """
        # make sure v_start is in the graph
        if not self.vertices_are_valid(v_start):
            return []

        # make a list of visited vertices
        visited = set()

        # make a dequeue of vertices to visit, used in loop
        to_visit = deque([v_start])

        # visit all direct successors of each vertex in order
        vertex = v_start
        while len(to_visit) != 0 and vertex != v_end:
            # get the next vertex
            vertex = to_visit.popleft()

            # mark this vertex as visited
            visited.add(vertex)

            # visit all unvisited direct successors and insert them into the queue
            successors_ordered = self.get_children(vertex)
            for successor in successors_ordered:
                # add this vertex to the itinerary for visiting later, in case it has unvisited descendants
                if successor not in visited and successor not in to_visit and self.adj_matrix[vertex][successor] > 0:
                    to_visit.append(successor)

        return visited

    def seek_cycle(self, vertex: int, exploring: set, explored: set) -> bool:
        """
        Based on https://stackoverflow.com/a/31543297/14257952
        :param vertex: string identifying the next vertex to visit
        :param exploring: set memoizing vertices whose child paths are still being explored
        :param explored: set memoizing fully explored vertices
        :return: True if a cycle was found; None otherwise
        """
        # mark this index as visited
        exploring.add(vertex)

        # recursive case: search all direct descendants, and visit all which are unvisited
        successors = self.adj_matrix[vertex]  # get the list of edges
        for next_vertex in range(len(successors)):  # get the vertices from the list
            # make sure this vertex actually is a child of the one being checked
            if self.adj_matrix[vertex][next_vertex] > 0:
                # base case 1: if this child vertex has been visited but its path isn't done being explored,
                # found a cycle
                if next_vertex in exploring:
                    return True

                # recursive case: if this child vertex is not fully explored, check its children
                elif next_vertex not in explored:
                    if self.seek_cycle(next_vertex, exploring, explored) is True:
                        return True

        # this vertex is done; mark it as done and continue searching
        explored.add(vertex)
        exploring.remove(vertex)

        # base case 2: visited all vertices in this connected component
        return False

    def has_cycle(self):
        """
        Detects whether the graph contains a cycle
        :return: True if the graph contains a cycle; False otherwise
        """
        # check every vertex in the graph for a cycle, in case graph is not a complete graph
        for v_start in self.get_vertices():
            if self.seek_cycle(v_start, set(), set()) is True:
                return True

        # passed the test; graph is acyclic
        return False

    def dijkstra(self, src: int) -> []:
        """
        Computes the length of the shortest path from a given vertex to all other vertices in the graph
        If a certain vertex is not reachable from src, its path's value is infinity
        :param src: int identifying the source vertex from which to measure paths
        :return: list with one value per vertex in the graph, where
            the value at index 0 is the length of the shortest path from vertex SRC to vertex 0,
            the value at index 1 is the length of the shortest path from vertex SRC to vertex 1, etc.
        """
        # track visited vertices. Vertices are stored as {vertex: min_distance_to_the_vertex}
        visited = {}

        # track vertices to be visited later
        to_visit = [(0, src)]  # paths are stored as (min_distance_to_vertex, vertex)
        heapify(to_visit)

        # find shortest distance to each node
        while len(to_visit) > 0:
            # get a vertex and its distance
            distance, vertex = heappop(to_visit)

            if vertex not in visited:
                # mark this vertex as visited
                visited[vertex] = distance

                # calculate heights for this vertex's children and set them to be visited later, for their children
                for successor in self.get_children(vertex):
                    child_distance = self.adj_matrix[vertex][successor]
                    total_distance = child_distance + distance  # min distance to this vertex
                    new_entry = (total_distance, successor)
                    heappush(to_visit, new_entry)

        # fill visited dict with infinities where it's missing an entry
        for vertex in self.get_vertices():
            if vertex not in visited:
                visited[vertex] = float('inf')

        # convert dict to list of distances, ordering by vertex
        list_out = []
        for vertex in sorted(visited):
            list_out.append(visited[vertex])

        return list_out


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

    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g)
    # for edge in edges:
    #     src, dst, weight = edge
    #     g.remove_edge(src, dst)
    #     print('after removing', src, '->', dst, '\n', g)

    # g = DirectedGraph()
    # print(g)
    # for vertex in range(10):
    #     g.add_vertex()
    #     print('after adding', vertex, '\n', g)
    #     print('vertices are')
    #     g.get_vertices()

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
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)

    edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    for src, dst in edges_to_remove:
        g.remove_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')

    edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    for src, dst in edges_to_add:
        g.add_edge(src, dst)
        print(g.get_edges(), g.has_cycle(), sep='\n')
    print('\n', g)
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
