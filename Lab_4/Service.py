from pqdict import PQDict


class GraphService(object):
    """
    This class manages the operation wanted using the RepoList class
    """

    def __init__(self, graph_repo):
        self._graph_repo = graph_repo

    def show_list_of_edges(self):
        # returns the list of edges from repository
        return self._graph_repo.show_edge()

    def show_out_dict(self):
        # returns the out-dictionary
        return self._graph_repo.show_out_edge_dict()

    def get_number_of_vertices(self):
        # returns the total number of vertices
        return self._graph_repo.get_number_of_vortexes()

    def list_of_outbound_edges_for_vertex(self, prime_vertex):
        """

        :param prime_vertex: integer
        :return: a list of edges that have as starting vertex the prime_vertex
        """
        prime_vertex = str(prime_vertex)
        list_of_edges = self.show_list_of_edges()
        list_of_neighbour_edges = []
        for edge in list_of_edges:
            if edge[0] == prime_vertex:
                list_of_neighbour_edges.append(edge)
        return list_of_neighbour_edges

    def check_if_a_vertex_has_no_links(self):
        """

        :return: True/False if there are/aren't isolated vertices
        """
        edge_dictionary = self.show_out_dict()
        for vertex in edge_dictionary:
            if not edge_dictionary[vertex]:
                return True
        return False

    def relax_edge(self, current_vertex, visited, ipq):
        """

        :param current_vertex: int
        :param visited: boolean list
        :param ipq: PQDict
        :return: executes an addition/update of an element in the queue
        """
        visited[current_vertex] = True
        list_of_neighbour_edges = self.list_of_outbound_edges_for_vertex(current_vertex)
        for edge in list_of_neighbour_edges:
            neighbour = int(edge[1])
            if not visited[neighbour]:
                if neighbour not in ipq:
                    ipq.additem(neighbour, edge)
                elif edge[2] < ipq[neighbour][2]:
                    ipq.updateitem(neighbour, edge)

    def prim_minimal_spanning_tree(self):
        """

        :return: the minimal spanning tree of the graph
        """
        if self.check_if_a_vertex_has_no_links():
            return None, None
        vertices_number = int(self.get_number_of_vertices())
        edge_number = vertices_number - 1
        edge_count, mst_cost = 0, 0
        visited = list()
        mst_edges = list()
        index_priority_queue = PQDict()
        for vertex in range(vertices_number):
            visited.append(False)
            if vertex < edge_number:
                mst_edges.append(None)
        self.relax_edge(0, visited, index_priority_queue)
        while bool(index_priority_queue) and edge_count != edge_number:
            new_ipq = sorted(index_priority_queue.items(), key=lambda kv: kv[1][2])
            neighbour_vertex, mst_edge = new_ipq[0]
            del index_priority_queue[neighbour_vertex]
            mst_edges[edge_count] = mst_edge
            edge_count += 1
            mst_cost += int(mst_edge[2])
            self.relax_edge(neighbour_vertex, visited, index_priority_queue)
        if edge_count != edge_number:
            return None, None
        else:
            return mst_edges, mst_cost
