class UI(object):

    def __init__(self, graph_service):
        self._graph_service = graph_service
        self._choices = {
            '1': self.show_list_of_edges,
            '2': self.show_in_degree_dict,
            '3': self.show_out_degree_dict,
            '4': self.show_number_of_vertices,
            '5': self.existence_of_edge_between_two_vertices,
            'd': self.get_in_and_out_degree_of_a_vertex,
            '6': self.list_the_outbound_edges,
            '7': self.list_the_inbound_edges,
            'e': self.retrieve_or_modify_the_cost_of_an_edge,
            '+': self.add_new_element,
            '-': self.remove_element,
            'c': self.copy_graph,
            'p': self.shortest_path,
            'D': self.dijkstra_shortest_path,
            'S': self.strong_connected
        }

    @staticmethod
    def menu():
        print("\nTo display the list of edges press 1")
        print("To display the list of in-degree vertexes and their edges press 2")
        print("To display the list of out-degree vertexes and their edges press 3")
        print("To see the number of vertices press 4")
        print("To see if there exist an edge between two vertices press 5")
        print("To check the degree for a specific vertex press d")
        print("To see the outbound edges and their targeted vertex press 6")
        print("To see the inbound edges and their origin vertex press 7")
        print("To see or modify the cost of an edge press e")
        print("To add a new vertex/edge press +")
        print("To remove a vertex/edge press -")
        print("To copy the graph to other file press c")
        print("To see the shortest path between two vertices starting from the end vertex, press p")
        print("To see the shortest cost path between two vertices with Dijkstra press D")
        print("To see the strongly connected components press S")
        print('\n')

    def show_list_of_edges(self):
        edges = self._graph_service.show_list_of_edges()
        for edge in edges:
            print(", ".join(edge))

    def show_in_degree_dict(self):
        in_degree = self._graph_service.show_in_dict()
        print("In-degree vertexes")
        for vertex in in_degree:
            print("   ", vertex, ":", in_degree[vertex])

    def show_out_degree_dict(self):
        out_degree = self._graph_service.show_out_dict()
        print("Out-degree vertexes")
        for vertex in out_degree:
            print("  ", vertex, ":", out_degree[vertex])

    def show_number_of_vertices(self):
        print("The number of vertices is: {}".format(self._graph_service.get_number_of_vertices()))

    def existence_of_edge_between_two_vertices(self):
        start_vertex = input("Write the start vertex: ")
        end_vertex = input("Write the end vertex: ")
        if self._graph_service.validation_of_edge(start_vertex, end_vertex):
            print("Yes, there is an edge between {} and {} vertex".format(start_vertex, end_vertex))
        else:
            print("No, there isn't an edge between {} and {} vertex".format(start_vertex, end_vertex))

    def get_in_and_out_degree_of_a_vertex(self):
        vertex_to_find = input("Write the vertex of which you want to do the search: ")
        print("To check the in degree press i")
        print("To check the out degree press o")
        command = input(">>> ")
        if command == 'i':
            in_degree = self._graph_service.in_degree_of_vertex(vertex_to_find)
            print("The in degree of the {} vertex is {}".format(vertex_to_find, in_degree))
        elif command == 'o':
            out_degree = self._graph_service.out_degree_of_vertex(vertex_to_find)
            print("The out degree of {} vertex is {}".format(vertex_to_find, out_degree))
        else:
            raise TypeError("Please insert one of the options, not something else")

    def list_the_outbound_edges(self):
        for edge in self._graph_service.list_outbound_edges():
            print("The edge with the cost {} has the vertex {} as target".format(edge[0], edge[1]))

    def list_the_inbound_edges(self):
        for edge in self._graph_service.list_inbound_edges():
            print("The edge with the cost {} has the vertex {} as origin".format(edge[0], edge[1]))

    def retrieve_or_modify_the_cost_of_an_edge(self):
        start_vertex = input("Type the start vertex: ")
        end_vertex = input("Type the end vertex: ")
        print("If you want to see the cost of the edge press c")
        print("If you want to modify the cost of the edge press m")
        command = input(">>> ")
        if command == 'c':
            print("The cost of the edge with the heads {} and {} is {}".format(start_vertex, end_vertex, self._graph_service.cost_of_specific_edge(start_vertex, end_vertex)))
        elif command == 'm':
            new_cost = input("Type the new cost of the edge: ")
            self._graph_service.update_cost_of_edge(start_vertex, end_vertex, new_cost)
        else:
            raise TypeError("Please choose one of the options")

    def add_new_element(self):
        print("To add a new vertex press v")
        print("To add a new edge press e")
        command = input(">>> ")
        if command == 'v':
            self._graph_service.add_a_new_vertex()
        elif command == 'e':
            start_vertex = input("Type the start vertex: ")
            end_vertex = input("Type the end vertex: ")
            cost = input("Type the cost of the new edge: ")
            self._graph_service.add_a_new_edge(start_vertex, end_vertex, cost)
        else:
            raise TypeError("Please choose one of the two options")

    def remove_element(self):
        print("To remove a vertex press v")
        print("To remove a edge press e")
        command = input(">>> ")
        if command == 'v':
            vertex_to_remove = input("Type the vertex you want removed: ")
            self._graph_service.remove_a_vertex(vertex_to_remove)
        elif command == 'e':
            start_vertex = input("Type the start vertex: ")
            end_vertex = input("Type the end vertex: ")
            self._graph_service.remove_a_edge(start_vertex, end_vertex)
        else:
            raise TypeError("Please choose one of the two options")

    def copy_graph(self):
        self._graph_service.copy_of_graph()

    def shortest_path(self):
        start_vertex = input("Please insert the start vertex: ")
        end_vertex = input("Please insert the end vertex: ")
        shortest_route = self._graph_service.find_the_shortest_path(start_vertex, end_vertex)
        if not shortest_route:
            print("There isn't a route between the vertices you want")
        else:
            print("The shortest route from vertex {} to vertex {} is:".format(start_vertex, end_vertex))
            for index in range(0, len(shortest_route)):
                if index != len(shortest_route) - 1:
                    print("{} -> ".format(shortest_route[index]), end=" ")
                else:
                    print(str(shortest_route[index]))
                    return

    def dijkstra_shortest_path(self):
        start_vertex = input("Please insert the start vertex: ")
        end_vertex = input("Please insert the end vertex: ")
        shortest_route = self._graph_service.shortest_cost_route_with_Dijsktra(start_vertex, end_vertex)
        print("The shortest route from vertex {} to vertex {} have a cost of {}".format(start_vertex, end_vertex, shortest_route))

    def strong_connected(self):
        components = self._graph_service.strongly_connected_components()
        print("The strongly connected components are: ")
        maximum_low_link_value = max(components)
        index = 0
        number_of_components = 0
        while index <= maximum_low_link_value:
            if index in components:
                for position in range(len(components)):
                    if index == components[position]:
                        print("\t{}".format(position), end=' ')
                print('\n')
                number_of_components += 1
            index += 1
        print("There are {} strongly connected components".format(number_of_components))

    def ui_main(self):
        while True:
            self.menu()
            index_of_choice = input("Choose the command you'd like to execute: ")
            if index_of_choice == "exit":
                return
            if index_of_choice in self._choices:
                self._choices[index_of_choice]()
            else:
                raise TypeError("Something went wrong! Please reenter your command")
