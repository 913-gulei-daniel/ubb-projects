"""
    Graph Class
"""

from exceptions import *
from random import randrange
from copy import deepcopy
import math


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
    minimum cost path
    """

    def bellman_ford(self, start, maxLen):
        """
        bellman-ford algorithm for getting the walk costs
        :param start: start vertex
        :param maxLen: the maximum length a walk can have
        :return: list of maps
        """
        initMap = {start:0}
        dist = [initMap]

        for k in range(1, maxLen + 1):
            prevMap = dist[k - 1]
            currMap = {}

            for y in prevMap:
                for x in self.neighbours_iterator(y):
                    if x not in currMap or currMap[x] > prevMap[y] + self.get_edge_cost(y, x):
                        currMap[x] = prevMap[y] + self.get_edge_cost(y, x)

            dist.append(currMap)

        return dist

    def min_cost_walk(self, start, end, maxLen):
        dist = self.bellman_ford(start, maxLen)
        sw = 0
        minim = math.inf
        verts = []
        for i in range(1, maxLen):
            if end in dist[i].keys():
                if sw == 0:
                    sw = 1
                    minim = dist[i][end]
                    verts = dist[i].keys()
                elif sw == 1 and minim > dist[i][end]:
                    minim = dist[i][end]
                    verts = dist[i].keys()

        return minim, verts


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



