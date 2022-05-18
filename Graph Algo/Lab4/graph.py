"""
    Graph Class
"""

from exceptions import *
from random import randrange
from copy import deepcopy
from queue import Queue


class UndirectedGraph:
    def __init__(self, n=0, m=0):
        self._vertices = set()
        self._neighbours = dict()
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

    def degree(self, vertex):
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

    def add_edge(self, vertex1, vertex2, edge_cost=0):
        """
        Adds an edge to the graph.
        """
        if self.is_edge(vertex1, vertex2):
            raise EdgeException("The given edge already exists")

        if not self.is_vertex(vertex1) or not self.is_vertex(vertex2):
            raise EdgeException("The vertices on the edge do not exist.")

        self._neighbours[vertex1].add(vertex2)
        self._neighbours[vertex2].add(vertex1)
        self._cost[(vertex1, vertex2)] = edge_cost

    def remove_edge(self, vertex1, vertex2):
        """
        Removes an edge from the graph.
        """
        if not self.is_edge(vertex1, vertex2):
            raise EdgeException("The given edge does not exist.")

        del self._cost[(vertex1, vertex2)]

        self._neighbours[vertex1].remove(vertex2)
        self._neighbours[vertex2].remove(vertex1)

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

        del self._neighbours[vertex]

        self._vertices.remove(vertex)

    def copy(self):
        """
        Returns a deepcopy of the graph.
        """
        return deepcopy(self)

    def find_set(self, vertex, parent):
        if parent[vertex] == vertex:
            return vertex
        return self.find_set(parent[vertex], parent)

    def union_set(self, parent, rank, first_vertex, second_vertex):
        first_vertex_root = self.find_set(first_vertex, parent)
        second_vertex_root = self.find_set(second_vertex, parent)

        if rank[first_vertex_root] < rank[second_vertex_root]:
            parent[first_vertex_root] = second_vertex_root
        elif rank[first_vertex_root] > rank[second_vertex_root]:
            parent[second_vertex_root] = first_vertex_root
        else:
            parent[second_vertex_root] = first_vertex_root
            rank[first_vertex_root] += 1

    def print_minimum_spanning_tree(self, minimum_spanning_tree):
        total_cost = 0
        for index in range(len(minimum_spanning_tree)):
            print("Edge ({0}, {1}) having the cost {2}".format(minimum_spanning_tree[index][0],
                                                               minimum_spanning_tree[index][1],
                                                               minimum_spanning_tree[index][2]))
            total_cost += minimum_spanning_tree[index][2]
        print("Total cost is: {0}\n".format(total_cost))


"""
    Random Graph Generator
"""


def random_graph(vertices_no, edges_no):
    g = UndirectedGraph()

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
    Kruskal
"""


def kruskal_algorithm(self):
    # I will create an array which contains each edge, and the cost of it, also I will create the parent set
    parent = [index for index in range(self.count_vertices())]
    rank = [0 for index in range(self.count_vertices())]
    edges = []
    minimum_spanning_tree = []
    for vert1, vert2, cost in self.edges_iterator():
        edges.append([vert1, vert2, cost])

    # I will sort the array of edges
    edges.sort(key=lambda element: element[2])
    index1 = 0
    index2 = 0
    while index2 < self.count_vertices() - 1:
        first_vertex, second_vertex, cost = edges[index1]
        index1 += 1
        vertex1 = self.find_set(first_vertex, parent)
        vertex2 = self.find_set(second_vertex, parent)

        if vertex1 != vertex2:
            index2 += 1
            minimum_spanning_tree.append([first_vertex, second_vertex, cost])
            self.union_set(parent, rank, vertex1, vertex2)

    self.print_minimum_spanning_tree(minimum_spanning_tree)

