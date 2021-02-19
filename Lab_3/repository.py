class Graph(object):

    def __init__(self):
        self._list_of_edges = []  # memorises the lines from file
        self._in_edge_dict = {}  # a list of in-edges for every vertex
        self._out_edge_dict = {}  # a list of out-edges for every vertex
        self._first_line = []  # keeps the number of vertices on the first position and the one of edges on the second
        self._number_of_copies = 1  # number of files made as a copy of the original
        self.create_the_in_and_out_dict()

    def update_edge(self, start_vertex, end_vertex, new_cost):
        """
        input: start_vertex, end_vertex, new_cost - char
        output: updates the cost of a specific edge
        """

        for edge in self._list_of_edges:
            if int(edge[0]) == int(start_vertex) and int(edge[1]) == int(end_vertex):
                edge[2] = new_cost
                return

    def add_vertex(self):
        """
        input:
        output: adds another vertex to the dictionaries of in and out dictionaries
                and increases by 1 the number of vertices
        """
        self._first_line[0] = str(int(self._first_line[0]) + 1)
        number_of_vertices = self.get_number_of_vortexes()
        self.add_in_edge_dict(int(number_of_vertices) + 1, [])
        self.add_out_edge_dict(int(number_of_vertices) + 1, [])

    def add_edge(self, new_edge):
        """
        input: new_edge - list
        output: adds another edge for a specific vertex from in/out dictionary and increases the number of edges
        """
        self._first_line[1] = str(int(self._first_line[1]) + 1)
        self._list_of_edges.append(new_edge)
        self._out_edge_dict[int(new_edge[0])].append([new_edge[1], new_edge[2]])
        self._in_edge_dict[int(new_edge[1])].append([new_edge[0], new_edge[2]])

    def remove_edge(self, edge_to_remove):
        """
        input: edge_to_remove - list
        output: decreases the number of edges, removes a specific edge from list of edges,
                then removes that edge from both dictionaries accordingly
        """

        self._first_line[1] = str(int(self._first_line[1]) - 1)

        for edge in self._list_of_edges:
            if edge[0] == edge_to_remove[0] and edge[1] == edge_to_remove[1]:
                self._list_of_edges.remove(edge)
                break

        for vertex in self._in_edge_dict:
            if vertex == int(edge_to_remove[1]):
                for edge in self._in_edge_dict[vertex]:
                    if edge[0] == edge_to_remove[0]:
                        self._in_edge_dict[vertex].remove(edge)
                        break

        for vertex in self._out_edge_dict:
            if vertex == int(edge_to_remove[0]):
                for edge in self._out_edge_dict[vertex]:
                    if edge[0] == edge_to_remove[1]:
                        self._out_edge_dict[vertex].remove(edge)
                        break

    def add_in_edge_dict(self, new_vortex, new_list_of_edges):
        """
        input: new_vertex - int; new_list_of_edges - list
        output: adds another vertex to the in-dictionary along with its list of edges
        """
        self._in_edge_dict[new_vortex] = new_list_of_edges

    def add_out_edge_dict(self, new_vortex, new_list_of_edge):
        """
        input: new_vertex - int; new_list_of_edges - list
        output: adds another vertex to the out-dictionary along with its list of edges
        """
        self._out_edge_dict[new_vortex] = new_list_of_edge

    def remove_vertex(self, vertex_to_remove):
        """
        input: vertex_to_remove - char
        output: removes a specific vertex along with its edges from dictionaries,
                removes all edges from the list of edges that intersect the vertex
                decreases the number of vertices by 1 and the number of edges by the number of edges removed
        """
        del self._in_edge_dict[int(vertex_to_remove)]
        del self._out_edge_dict[int(vertex_to_remove)]

        edges_to_remove = 0
        for edge in self._list_of_edges:
            if edge[0] == vertex_to_remove or edge[1] == vertex_to_remove:
                edges_to_remove += 1

        self._first_line[0] = str(int(self._first_line[0]) - 1)
        self._first_line[1] = str(int(self._first_line[1]) - edges_to_remove)

        while edges_to_remove > 0:
            for edge in self._list_of_edges:
                if edge[0] == vertex_to_remove or edge[1] == vertex_to_remove:
                    self._list_of_edges.remove(edge)
                    edges_to_remove -= 1

    def show_edge(self):
        # returns the list of edges
        return self._list_of_edges

    def show_in_edge_dict(self):
        # returns the dictionary that has the in-edges for every vertex
        return self._in_edge_dict

    def show_out_edge_dict(self):
        # returns the dictionary that has the out-edges for every vertex
        return self._out_edge_dict

    def get_number_of_vortexes(self):
        # returns the number of vertices
        number_of_vertices = self._first_line[0]
        return number_of_vertices

    def search_vortex_for_in_degree(self, vortex_to_search_for):
        """
        input: vertex_to_search_for - char
        output: returns the list of edges that comes into the vertex
        """
        in_degree_list = []
        for elements in self._list_of_edges:
            if int(elements[1]) == int(vortex_to_search_for):
                in_degree_list.append([elements[0], elements[2]])
        return in_degree_list

    def search_vortex_for_out_degree(self, vortex_to_search_for):
        """
        input: vertex_to_search_for - char
        output: returns the list of edges that comes out of the vertex
        """
        out_degree_list = []
        for elements in self._list_of_edges:
            if int(elements[0]) == int(vortex_to_search_for):
                out_degree_list.append([elements[1], elements[2]])
        return out_degree_list

    def create_the_in_and_out_dict(self):
        """
        input:
        output: creates the dictionaries of in/out edges for every degree
        """
        number_of_vortexes = self.get_number_of_vortexes()
        for vortex_index in range(0, int(number_of_vortexes)):
            self.add_in_edge_dict(vortex_index, self.search_vortex_for_in_degree(vortex_index))
            self.add_out_edge_dict(vortex_index, self.search_vortex_for_out_degree(vortex_index))

    def create_copy_of_graph(self):
        """
        input:
        output: creates a file that contains the copy of the original graph
        """
        file_copy = open("graph_copy_" + str(self._number_of_copies) + ".txt", 'w+')
        first_line = self.write_first_line(self._first_line) + '\n'
        file_copy.write(first_line)
        for line_index in range(int(self._first_line[1])):
            line = self.write_line(self._list_of_edges[line_index]) + '\n'
            file_copy.write(line)
        file_copy.close()
        self._number_of_copies += 1

    @staticmethod
    def read_first_line(line):
        #  reads line from file and returns in the wanted format
        parts = line.split()
        return [parts[0].strip(), parts[1].strip()]

    @staticmethod
    def write_first_line(entity):
        #  writes a line in the desired format
        return str(entity[0]) + " " + str(entity[1])

    @staticmethod
    def read_line(line):
        #  reads a line from file and returns it in the wanted format
        parts = line.split()
        return [parts[0].strip(), parts[1].strip(), parts[2].strip()]

    @staticmethod
    def write_line(entity):
        #  writes a line in the desired format
        return str(entity[0]) + " " + str(entity[1]) + " " + str(entity[2])


"""
 Class to operate with files
"""


class GraphFile(Graph):

    def __init__(self, filename, read_graph, write_graph, read_first_line, write_first_line):
        self._filename = filename
        self._read_graph = read_graph
        self._write_graph = write_graph
        self._read_first_line = read_first_line
        self._write_first_line = write_first_line
        Graph.__init__(self)

    def _read_from_file(self):
        """
        input:
        output: reads data from file and constructs the lists of edges and number of vertices and
                the number of edges used forward into the program
        """
        self._first_line = list
        self._list_of_edges = []
        with open(self._filename, 'r') as file:
            first_line = file.readline()
            first_line = first_line.strip()
            first_line = self._read_first_line(first_line)
            self._list_of_edges.append(first_line)
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    entity = self._read_graph(line)
                    self._list_of_edges.append(entity)
            self._first_line = self._list_of_edges[0]
            del self._list_of_edges[0]

    def _write_to_file(self):
        """
        input:
        output: writes the edges from the list into the file
        """
        with open(self._filename, 'w') as file:
            first_line = self._write_first_line(self._first_line)
            file.write(first_line + '\n')
            for entity in self._list_of_edges:
                line = self._write_graph(entity)
                file.write(line + '\n')

    def add_edge(self, new_edge):
        # overwrites the function of addition of an edge into the list
        self._read_from_file()
        Graph.add_edge(self, new_edge)
        self._write_to_file()

    def show_edge(self):
        # overwrites the function that returns the list of edges
        self._read_from_file()
        return Graph.show_edge(self)

    def create_the_in_and_out_dict(self):
        # overwrites the function that creates the in/out dictionaries
        self._read_from_file()
        Graph.create_the_in_and_out_dict(self)

    def remove_vertex(self, vertex_to_remove):
        # overwrites the function that removes a vertex from the graph
        self._read_from_file()
        Graph.remove_vertex(self, vertex_to_remove)
        self._write_to_file()
