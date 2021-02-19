class GraphService(object):
    """
    This class manages the operation wanted using the RepoList class
    """
    def __init__(self, graph_repo):
        self._graph_repo = graph_repo

    def show_list_of_edges(self):
        # returns the list of edges from repository
        return self._graph_repo.show_edge()

    def show_in_dict(self):
        # returns the in-dictionary
        return self._graph_repo.show_in_edge_dict()

    def show_out_dict(self):
        # returns the out-dictionary
        return self._graph_repo.show_out_edge_dict()

    def get_number_of_vertices(self):
        # returns the total number of vertices
        return self._graph_repo.get_number_of_vortexes()

    def validation_of_edge(self, start_vertex, end_vertex):
        """
        input : start_vertex, end_vertex - char
        output: tests if in the list of edges we have an edge between the two vertices received
        """
        list_of_edges = self._graph_repo.show_edge()
        for edge in list_of_edges:
            if edge[0] == start_vertex and edge[1] == end_vertex:
                return True
        return False

    def in_degree_of_vertex(self, vertex):
        """
        input: vertex - char
        output: returns the number of in-edges that are coming into a specific vertex
        """
        in_dict = self._graph_repo.show_in_edge_dict()
        counter_of_in_degree = 0
        for key in in_dict:
            if int(key) == int(vertex):
                counter_of_in_degree += len(in_dict[key])
        return counter_of_in_degree

    def out_degree_of_vertex(self, vertex):
        """
        input: vertex - char
        output: returns the number of out-edges that are coming out from a specific vertex
        """
        out_dict = self._graph_repo.show_out_edge_dict()
        counter_of_out_degree = 0
        for key in out_dict:
            if int(key) == int(vertex):
                counter_of_out_degree += len(out_dict[key])
        return counter_of_out_degree

    def list_outbound_edges(self):
        """
        input:
        output: returns a list containing the outbound edges and their targeted vertex
        """
        list_of_edges = self._graph_repo.show_edge()
        list_of_outbound_edges_and_their_target = []
        for edge in list_of_edges:
            list_of_outbound_edges_and_their_target.append([edge[2], edge[1]])
        return list_of_outbound_edges_and_their_target

    def list_inbound_edges(self):
        """
        input:
        output: returns a list containing the inbound edges and their origin vertex
        """
        list_of_edges = self._graph_repo.show_edge()
        list_of_inbound_edges_and_their_target = []
        for edge in list_of_edges:
            list_of_inbound_edges_and_their_target.append([edge[2], edge[0]])
        return list_of_inbound_edges_and_their_target

    def update_cost_of_edge(self, start_vertex, end_vertex, new_cost):
        """
        input: start_vertex, end_vertex, new_cost - char
        output: sends the parameters to repository in order to update an edge
        """
        return self._graph_repo.update_edge(start_vertex, end_vertex, new_cost)

    def cost_of_specific_edge(self, start_vertex, end_vertex):
        """
        input: start_edge, end_edge - char
        output: returns the cost of a specific edge
        """
        list_of_edges = self._graph_repo.show_edge()
        for edge in list_of_edges:
            if int(edge[0]) == int(start_vertex) and int(edge[1]) == int(end_vertex):
                return edge[2]

    def add_a_new_vertex(self):
        """
        input:
        output: goes into repository where adds a new vertex
        """
        self._graph_repo.add_vertex()

    def add_a_new_edge(self, start_vertex, end_vertex, cost):
        """
        input: start_vertex, end_vertex, cost - char
        output: goes to repository where adds a new edge using the data from the parameters
        """
        self._graph_repo.add_edge([start_vertex, end_vertex, cost])

    def remove_a_edge(self, start_vertex, end_vertex):
        """
        input: start_vertex, end_vertex - char
        output: goes to repository where it removes an edge using the data from the parameters
        """
        self._graph_repo.remove_edge([start_vertex, end_vertex])

    def remove_a_vertex(self, vertex_to_remove):
        """
        input: vertex_to_remove - char
        output: goes to repository and removes a specific vertex
        """
        self._graph_repo.remove_vertex(vertex_to_remove)

    def copy_of_graph(self):
        """
        input:
        output: goes to repository where creates a copy of the current graph
        """
        self._graph_repo.create_copy_of_graph()

