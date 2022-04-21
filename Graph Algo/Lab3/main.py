"""
    UI Class and start of program
"""

from graph import *


class UI:
    def __init__(self):
        self.graph = None

    def create_empty_graph(self):
        self.graph = Graph()
        print("UndirectedGraph Emptied")

    def create_edgeless_graph(self):
        n = input("Enter number of vertices: ")

        try:
            self.graph = Graph(int(n))
            print("UndirectedGraph Created")

        except Exception as e:
            print(e)

    def create_random_graph(self):
        n = input("Enter number of vertices: ")
        m = input("Enter number of edges:  ")

        try:
            self.graph = Graph(int(n), int(m))
            print("UndirectedGraph Created")

        except Exception as e:
            print(e)

    def add_vertex(self):
        n = input("Type the vertex you wish to add: ")

        try:
            self.graph.add_vertex(int(n))

        except Exception as e:
            print(e)

    def add_edge(self):
        v1 = input("Enter the first vertex: ")
        v2 = input("Enter the second vertex: ")
        c = input("Enter the cost: ")

        try:
            self.graph.add_edge(int(v1), int(v2), int(c))

        except Exception as e:
            print(e)

    def remove_vertex(self):
        n = input("Enter vertex number to remove: ")

        try:
            self.graph.remove_vertex(int(n))

        except Exception as e:
            print(e)

    def remove_edge(self):
        v1 = input("Enter the first vertex: ")
        v2 = input("Enter the second vertex: ")

        try:
            self.graph.remove_edge(int(v1), int(v2))

        except Exception as e:
            print(e)

    def degree(self):
        n = input("Enter vertex number: ")

        try:
            print(self.graph.degree(int(n)))

        except Exception as e:
            print(e)

    def get_vertices(self):
        print("There are a total of " + str(self.graph.count_vertices()) + " vertices.")

    def get_edges(self):
        print("There are a total of " + str(self.graph.count_edges()) + " edges.")

    def print_vertex_list(self):
        for node in self.graph.vertices_iterator():
            print(node, end=" ")

        print()

    def print_neighbour_list(self):
        n = input("Enter vertex number: ")

        try:
            ok = False

            for node in self.graph.neighbours_iterator(int(n)):
                print(node, end=" ")
                ok = True

            if not ok:
                print("Vertex " + str(n) + " has no neighbours.")

            else:
                print()

        except Exception as e:
            print(e)

    def print_edges(self):
        ok = False

        for triple in self.graph.edges_iterator():
            print("Vertices " + str(triple[0]) + ", " + str(triple[1]) + " -> cost: " + str(triple[2]) + ".")
            ok = True

        if not ok:
            print("No edges in the graph.")

    def read_file(self):
        path = input("Enter file name: ")

        try:
            self.graph = read_file(path)

        except Exception as e:
            print(e)

    def write_file(self):
        path = input("Enter file name: ")

        try:
            write_file(path, self.graph)

        except Exception as e:
            print(e)

    def copy(self):
        g_copy = self.graph.copy
        self.create_empty_graph()

        self.print_vertex_list()
        print()

        self.graph = g_copy

        self.print_vertex_list()

    def lcw(self):
        start = input("Enter starting vertex: ")
        end = input("Enter end vertex: ")

        print(lowest_cost_walk(self.graph, int(start), int(end)), end="\n\n")

    def start(self):
        commands = {"1": self.create_empty_graph,
                    "2": self.create_edgeless_graph,
                    "3": self.create_random_graph,
                    "4": self.add_vertex,
                    "5": self.add_edge,
                    "6": self.remove_vertex,
                    "7": self.remove_edge,
                    "8": self.degree,
                    "9": self.get_vertices,
                    "10": self.get_edges,
                    "11": self.print_vertex_list,
                    "12": self.print_neighbour_list,
                    "13": self.print_edges,
                    "14": self.read_file,
                    "15": self.write_file,
                    "16": self.copy,
                    "17": self.lcw}

        while True:
            print("1. Generate an empty graph")
            print("2. Generate a graph with n vertices")
            print("3. Generate a graph with n vertices and m random edges")
            print("4. Add a vertex")
            print("5. Add an edge")
            print("6. Remove a vertex")
            print("7. Remove an edge")
            print("8. Print the in degree of a vertex")
            print("9. Print the number of vertices")
            print("10. Print the number of edges")
            print("11. Print the list of vertices")
            print("12. Print the list of neighbours of a vertex")
            print("13. Print the list of edges")
            print("14. Reads the graph from a file")
            print("15. Writes the graph to a file")
            print("16. Copy the old graph")
            print("17. Find the Lowest Cost Walk between two vertices")
            print("0. Exit")

            cmd = input()

            if cmd in commands:
                commands[cmd]()
                print()

            elif cmd == "0":
                break

            else:
                print("Invalid command.")


"""
    File I/O
"""


def read_file(file_path):
    file = open(file_path, "r")
    n, m = map(int, file.readline().split())
    g = Graph(n)

    for _ in range(m):
        vertex1, vertex2, edge_cost = map(int, file.readline().split())
        g.add_edge(vertex1, vertex2, edge_cost)

    file.close()

    return g


def write_file(file_path, g):
    file = open(file_path, "w")
    file.write(str(g.count_vertices()) + " " + str(g.count_edges()))

    for node in g.vertices_iterator():
        for neighbour in g.neighbours_iterator(node):
            file.write(str(node) + " " + str(neighbour) + " " + str(g.get_edge_cost(node, neighbour) + "\n"))

    file.close()


UI().start()
