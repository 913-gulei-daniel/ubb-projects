"""
    Graph Class
"""

from exceptions import *
from random import randrange
from copy import deepcopy


class Graph:
    def __init__(self, n=0, m=0):
        self._vertices = set()
        self._neighbours = dict()
        self._transpose = dict()
        self._cost = dict()

        for i in range(n):
            self.add_vertex(i)

        for j in range(m):
            vertex1 = randrange(n)
            vertex2 = randrange(n)

            while self.is_edge(vertex1, vertex2):
                vertex1 = randrange(n)
                vertex2 = randrange(n)

            self.add_edge(vertex1, vertex2, randrange(20))

    def vertices_iterator(self):
        """
        Returns an iterator to the set of vertices.
        """
        for vertex in self._vertices:
            yield vertex

    def neighbours_iterator(self, vertex):
        """
        Returns an iterator to the set of (outbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexException("Invalid vertex.")

        for neighbour in self._neighbours[vertex]:
            yield neighbour

    def transpose_iterator(self, vertex):
        """
        Returns an iterator to the set of (inbound) neighbours of a vertex.
        """
        if not self.is_vertex(vertex):
            raise VertexException("Invalid vertex.")

        for neighbour in self._transpose[vertex]:
            yield neighbour

    def edges_iterator(self):
        """
        Returns an iterator to the set of edges.
        """
        for key, value in self._cost.items():
            yield key[0], key[1], value

    def is_vertex(self, vertex):
        """
        Returns True if the given vertex belongs to the graph.
        """
        return vertex in self._vertices

    def is_edge(self, vertex1, vertex2):
        """
        Returns True if the edge from vertex1 to vertex2 belongs to the graph.
        """
        return vertex1 in self._neighbours and vertex2 in self._neighbours[vertex1]

    def count_vertices(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self._vertices)

    def count_edges(self):
        """
        Returns the number of edges in the graph.
        """
        return len(self._cost)

    def in_degree(self, vertex):
        """
        Returns the number of edges with the endpoint vertex.
        """
        if vertex not in self._transpose:
            raise VertexException("The given vertex does not exist.")

        return len(self._transpose[vertex])

    def out_degree(self, vertex):
        """
        Returns the number of edges with the start point vertex.
        """
        if vertex not in self._neighbours:
            raise VertexException("The given vertex does not exist.")

        return len(self._neighbours[vertex])

    def get_edge_cost(self, vertex1, vertex2):
        """
        Returns the cost of an edge if it exists.
        """
        if (vertex1, vertex2) not in self._cost:
            raise EdgeException("The given edge does not exist.")

        return self._cost[(vertex1, vertex2)]

    def set_edge_cost(self, vertex1, vertex2, new_cost):
        """
        Sets the cost of an edge in the graph if it exists.
        """
        if (vertex1, vertex2) not in self._cost:
            raise EdgeException("The given edge does not exist.")

        self._cost[(vertex1, vertex2)] = new_cost

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        if self.is_vertex(vertex):
            raise VertexException("Cannot add a vertex which already exists.")

        self._vertices.add(vertex)
        self._neighbours[vertex] = set()
        self._transpose[vertex] = set()

    def add_edge(self, vertex1, vertex2, edge_cost=0):
        """
        Adds an edge to the graph.
        """
        if self.is_edge(vertex1, vertex2):
            raise EdgeException("The given edge already exists")

        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise EdgeException("The vertices on the edge do not exist.")

        self._neighbours[vertex1].add(vertex2)
        self._transpose[vertex2].add(vertex1)
        self._cost[(vertex1, vertex2)] = edge_cost

    def remove_edge(self, vertex1, vertex2):
        """
        Removes an edge from the graph.
        """
        if not self.is_edge(vertex1, vertex2):
            raise EdgeException("The given edge does not exist.")

        del self._cost[(vertex1, vertex2)]

        self._neighbours[vertex1].remove(vertex2)
        self._transpose[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph.
        """
        if not self.is_vertex(vertex):
            raise VertexException("Can't remove a vertex that doesn't exist.")

        to_remove = []

        for node in self._neighbours[vertex]:
            to_remove.append(node)

        for node in to_remove:
            self.remove_edge(vertex, node)

        to_remove = []

        for node in self._transpose[vertex]:
            to_remove.append(node)

        for node in to_remove:
            self.remove_edge(node, vertex)

        del self._neighbours[vertex]
        del self._transpose[vertex]

        self._vertices.remove(vertex)

    def copy(self):
        """
        Returns a deepcopy of the graph.
        """
        return deepcopy(self)


"""
    Random Graph Generator
"""


def random_graph(vertices_no, edges_no):
    g = Graph()

    for i in range(vertices_no):
        g.add_vertex(i)

    for j in range(edges_no):
        vertex1 = randrange(vertices_no)
        vertex2 = randrange(vertices_no)

        while g.is_edge(vertex1, vertex2):
            vertex1 = randrange(vertices_no)
            vertex2 = randrange(vertices_no)

        g.add_edge(vertex1, vertex2, randrange(20))


"""
    Floyd Warshall Lowest Cost Walk
"""

INF = 99999


def lowest_cost_walk(graph, start, end):
    if not graph.is_vertex(start):
        raise VertexException("Starting Vertex doesn't exist.\n")

    if not graph.is_vertex(end):
        raise VertexException("End Vertex doesn't exist.\n")

    if start == end:
        raise VertexException("The input Vertices are the same.\n")

    # distance matrix
    distance = []
    for vertex1 in graph.vertices_iterator():
        new_line_distance = []
        for vertex2 in graph.vertices_iterator():
            if graph.is_edge(vertex1, vertex2):
                new_line_distance.append(graph.get_edge_cost(vertex1, vertex2))
            elif vertex1 == vertex2:
                new_line_distance.append(0)
            else:
                new_line_distance.append(INF)
        distance.append(new_line_distance)

    # previous matrix
    previous = []
    for vertex1 in graph.vertices_iterator():
        new_line_previous = []
        for vertex2 in graph.vertices_iterator():
            if graph.is_edge(vertex1, vertex2):
                new_line_previous.append(vertex1)
            else:
                new_line_previous.append(-1)  # fill in with -1 if there is no predecessor
        previous.append(new_line_previous)

    for intermediateVertex in graph.vertices_iterator():
        # consider each vertex as an intermediate vertex
        for vertex1 in graph.vertices_iterator():
            # consider each vertex as source vertex
            for vertex2 in graph.vertices_iterator():
                # consider each vertex as destination vertex
                if distance[vertex1][intermediateVertex] + distance[intermediateVertex][vertex2] < distance[vertex1][vertex2]:
                    distance[vertex1][vertex2] = distance[vertex1][intermediateVertex] + distance[intermediateVertex][vertex2]
                    previous[vertex1][vertex2] = previous[intermediateVertex][vertex2]

    lowest_cost_path = distance[start][end]
    if lowest_cost_path == INF:
        raise VertexException("There is no path between the vertices.")

    reconstructed_path = reconstruct_path(previous, distance, start, end)

    return reconstructed_path, lowest_cost_path


def reconstruct_path(previous, distance, start, end):
    """
    Reconstructs the path with costs backwards using the previous matrix.
    input:
        - matrix previous
        - matrix distance
        - int startVertex
        - int endVertex
    output:
        - a list containing the edges from the lowest cost walk and its costs
    """

    path = [end]

    while end != start:
        end = previous[start][end]
        path.append(end)

    path.reverse()
    path_with_costs = []
    for indexVertex in range(len(path) - 1):
        path_with_costs.append(
            ((path[indexVertex], path[indexVertex + 1]), distance[path[indexVertex]][path[indexVertex + 1]]))

    return path_with_costs
