import random
from repository import GraphFile, Graph
from service import GraphService
from UI import UI

'''
    This function creates a random graph which will be stored in a file.
    It uses two inputs from the user, a number of vertices and a number of edges
'''


def create_random_graph():
    number_of_vertices = int(input("Type the number of vertices: "))
    number_of_edges = int(input("Type the number of edges: "))
    probable_id_for_vertex = list(range(number_of_vertices))
    probable_cost_for_vertex = []
    for index in range(number_of_edges + 1):
        new_cost = random.randrange(0, number_of_edges + 100, 2)
        probable_cost_for_vertex.append(new_cost)
    random_file = open("random_graph", 'w+')
    first_line = str(number_of_vertices) + " " + str(number_of_edges) + " \n"
    random_file.write(first_line)
    for line_index in range(number_of_edges):
        start_vertex_id = random.randrange(len(probable_id_for_vertex))
        start_vertex = str(probable_id_for_vertex[start_vertex_id])
        end_vertex_id = random.randrange(len(probable_id_for_vertex))
        end_vertex = str(probable_id_for_vertex[end_vertex_id])
        cost_id = random.randrange(len(probable_cost_for_vertex))
        cost = str(probable_cost_for_vertex[cost_id])
        line = start_vertex + " " + end_vertex + " " + cost + '\n'
        random_file.write(line)
    random_file.close()


'''
    From the start of the application the user has two choices
    To use a random graph or to use a specific one
'''


def choice():
    print("If you want to work with a random graph press 1")
    print("If you want to work with a specific graph press 2")
    command = input(">>> ")
    if command == '1':
        create_random_graph()
        repo = GraphFile("random_graph", Graph.read_line, Graph.write_line, Graph.read_first_line,
                         Graph.write_first_line)
        service = GraphService(repo)
        console = UI(service)
        console.ui_main()
    elif command == '2':
        repo = GraphFile("graph", Graph.read_line, Graph.write_line, Graph.read_first_line, Graph.write_first_line)
        service = GraphService(repo)
        console = UI(service)
        console.ui_main()
    else:
        raise TypeError("Please choose one of the above")


choice()
