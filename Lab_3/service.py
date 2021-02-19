from queue import Queue, LifoQueue
import math
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

    def compose_list_of_neighbours_for_vertex_from_in_dictionary(self, central_vertex):
        """
        input:  central_vertex-int
        output: list of direct neighbours
        """
        list_of_direct_neighbours = []
        in_dictionary = self.show_in_dict()
        for element_list in range(0, len(in_dictionary[central_vertex])):
            neighbour = in_dictionary[central_vertex][element_list][0]
            list_of_direct_neighbours.append(int(neighbour))
        return list_of_direct_neighbours

    def backward_route_of_course(self, start_vertex, end_vertex):
        """
        input: start_vertex, end_vertex - char
        output: list of elements to go through to reach end vertex from the start vertex
        """
        destination_found = False
        number_of_vertices = int(self.get_number_of_vertices())
        queue_of_vertices = Queue(maxsize=number_of_vertices)
        queue_of_vertices.put(int(end_vertex))
        previous = list()
        visited = list()
        for index in range(number_of_vertices):
            previous.append(None)
            visited.append(False)
        visited[int(end_vertex)] = True
        while not queue_of_vertices.empty():
            source_node = queue_of_vertices.get()
            neighbours = self.compose_list_of_neighbours_for_vertex_from_in_dictionary(int(source_node))

            for vertex in neighbours:
                if not visited[vertex]:
                    queue_of_vertices.put(int(vertex))
                    visited[vertex] = True
                    previous[int(vertex)] = source_node
                    if vertex == end_vertex:
                        destination_found = True
            if destination_found:
                break
        return previous

    def find_the_shortest_path(self, start_vertex, end_vertex):
        """
        :param start_vertex, end_vertex - char
        :return: list containing the vertices for the shortest route from start_vertex to end_vertex
        """
        previous = self.backward_route_of_course(start_vertex, end_vertex)
        shortest_route = [int(start_vertex)]
        if previous[0] == None:
            return []
        while True:
            vertex_to_add = previous[int(start_vertex)]
            shortest_route.append(vertex_to_add)
            if vertex_to_add == int(end_vertex):
                return shortest_route
            start_vertex = vertex_to_add

    def create_list_of_in_neighbours_from_vertex(self, central_vertex):
        """
        input:  central_vertex-int
        output: list of direct neighbours and the edge's cost between them
        """
        list_of_direct_neighbours = []
        in_dictionary = self.show_out_dict()
        for element_list in range(0, len(in_dictionary[central_vertex])):
            neighbour = in_dictionary[central_vertex][element_list]
            list_of_direct_neighbours.append(neighbour)
        return list_of_direct_neighbours

    def shortest_cost_route_with_Dijsktra(self, start_vertex, end_vertex):
        """
        :param start_vertex: char, end_vertex: char
        :return: the shortest route regarding the cost of edges
        """
        number_of_vertices = int(self.get_number_of_vertices())
        visited = list()
        distance = list()
        indexed_priority_queue = PQDict({start_vertex: 0})
        for index in range(number_of_vertices):
            visited.append(False)
            distance.append(math.inf)
        distance[int(start_vertex)] = 0
        while bool(indexed_priority_queue):
            current_vertex, minimum_value = indexed_priority_queue.popitem()
            print("Current: {}".format(current_vertex))
            print(distance)
            print(visited)
            print(indexed_priority_queue)

            minimum_value = int(minimum_value)
            visited[int(current_vertex)] = True
            if current_vertex == int(end_vertex):
                return distance[int(end_vertex)]
            if distance[int(current_vertex)] >= minimum_value:
                list_of_neighbours = self.create_list_of_in_neighbours_from_vertex(int(current_vertex))
                for neighbour in list_of_neighbours:
                    neighbour_key = int(neighbour[0])
                    neighbour_cost = int(neighbour[1])
                    if not visited[neighbour_key]:
                        new_distance = distance[int(current_vertex)] + neighbour_cost
                        if new_distance < distance[neighbour_key]:
                            distance[neighbour_key] = new_distance
                            if neighbour_key not in indexed_priority_queue:
                                indexed_priority_queue.additem(neighbour_key, new_distance)
                            else:
                                indexed_priority_queue.updateitem(neighbour_key, new_distance)

    def create_list_of_out_neighbours(self, central_vertex):
        """
        input:  central_vertex-int
        output: list of direct neighbours
        """
        list_of_direct_neighbours = []
        out_dictionary = self.show_out_dict()
        for element_list in range(0, len(out_dictionary[central_vertex])):
            neighbour = int(out_dictionary[central_vertex][element_list][0])
            list_of_direct_neighbours.append(neighbour)
        return list_of_direct_neighbours

    def dfs(self, current_id, on_stack, queue_of_vertices, ids, low, id):
        """

        :param current_id: int
        :param on_stack: list
        :param queue_of_vertices: LIFO queue
        :param ids: list
        :param low: list
        :param id: int
        :return: creates the strongly connected components by iterating through the neighbours of every vertex
        """
        list_of_neighbours = self.create_list_of_out_neighbours(current_id)
        queue_of_vertices.put(current_id)
        on_stack[current_id] = True
        ids[current_id] = low[current_id] = id
        id += 1
        for neighbour in list_of_neighbours:
            if ids[neighbour] == -1:
                self.dfs(neighbour, on_stack, queue_of_vertices, ids, low, id)
            if on_stack[neighbour]:
                low[current_id] = min(low[current_id], low[neighbour])
        if ids[current_id] == low[current_id]:
            while True:
                vertex = queue_of_vertices.get()
                on_stack[vertex] = False
                low[vertex] = ids[current_id]
                if vertex == current_id:
                    break

    def strongly_connected_components(self):
        """

        :return: the list of strongly connected components
        """
        unvisited = -1
        number_of_vertices = int(self.get_number_of_vertices())
        id = 0
        ids = list()
        low = list()
        on_stack = list()
        queue_of_vertices = LifoQueue(maxsize=number_of_vertices - 1)
        for index in range(number_of_vertices):
            ids.append(unvisited)
            low.append(0)
            on_stack.append(False)
        for current_id in range(number_of_vertices):
            if ids[current_id] == unvisited:
                self.dfs(current_id, on_stack, queue_of_vertices, ids, low, id)
        return low
