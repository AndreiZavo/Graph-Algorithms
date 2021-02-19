class UI(object):

    def __init__(self, graph_service):
        self._graph_service = graph_service
        self._choices = {
            '1': self.show_list_of_edges,
            '2': self.show_out_degree_dict,
            '3': self.show_number_of_vertices,
            '4': self.show_minimal_spanning_tree,
        }

    @staticmethod
    def menu():
        print("\nTo display the list of edges press 1")
        print("To display the list of vertices neighbours and their edge's cost press 2")
        print("To see the number of vertices press 3")
        print("To see the minimal spanning tree press 4")
        print('\n')

    def show_list_of_edges(self):
        edges = self._graph_service.show_list_of_edges()
        for edge in edges:
            print(", ".join(edge))

    def show_out_degree_dict(self):
        out_degree = self._graph_service.show_out_dict()
        print("Out-degree vertexes")
        for vertex in out_degree:
            print("  ", vertex, ":", out_degree[vertex])

    def show_number_of_vertices(self):
        print("The number of vertices is: {}".format(int(self._graph_service.get_number_of_vertices()) + 1))

    def show_minimal_spanning_tree(self):
        spanning_tree, sum_of_costs = self._graph_service.prim_minimal_spanning_tree()
        if spanning_tree is None:
            print("It is impossible to create a spanning tree")
        else:
            print("The edges that make the spanning tree are:")
            print(spanning_tree)
            print("The total cost of the edges is: {}".format(sum_of_costs))

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
