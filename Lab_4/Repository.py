class Graph(object):

    def __init__(self):
        self._list_of_edges = []  # memorises the lines from file
        self.edge_dict = {}  # a list of out-edges for every vertex
        self._first_line = []  # keeps the number of vertices on the first position and the one of edges on the second
        self.create_edge_dict()

    def add_edge_dict(self, new_vortex, new_list_of_edge):
        """
        input: new_vertex - int; new_list_of_edges - list
        output: adds another vertex to the out-dictionary along with its list of edges
        """
        self.edge_dict[new_vortex] = new_list_of_edge

    def show_edge(self):
        # returns the list of edges
        return self._list_of_edges

    def show_out_edge_dict(self):
        # returns the dictionary that has the out-edges for every vertex
        return self.edge_dict

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

    def create_edge_dict(self):
        """
        input:
        output: creates the dictionaries of in/out edges for every degree
        """
        number_of_vortexes = self.get_number_of_vortexes()
        for vortex_index in range(0, int(number_of_vortexes)):
            self.add_edge_dict(vortex_index, self.search_vortex_for_out_degree(vortex_index))

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
    def read_reverse_line(line):
        # reads a line from a file and returns it as an edge from the end_vertex to the start_vertex but with the
        # same cost
        parts = line.split()
        return [parts[1].strip(), parts[0].strip(), parts[2].strip()]


"""
 Class to operate with files
"""


class GraphFile(Graph):

    def __init__(self, filename, read_graph, reverse_graph, read_first_line):
        self._filename = filename
        self._read_graph = read_graph
        self._read_reverse_graph = reverse_graph
        self._read_first_line = read_first_line
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
                    reverse_entity = self._read_reverse_graph(line)
                    self._list_of_edges.append(entity)
                    self._list_of_edges.append(reverse_entity)
            self._first_line = self._list_of_edges[0]
            del self._list_of_edges[0]

    def show_edge(self):
        # overwrites the function that returns the list of edges
        self._read_from_file()
        return Graph.show_edge(self)

    def create_edge_dict(self):
        # overwrites the function that creates the in/out dictionaries
        self._read_from_file()
        Graph.create_edge_dict(self)
