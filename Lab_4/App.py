from Repository import GraphFile, Graph
from Service import GraphService
from UI import UI


def choice():
    repo = GraphFile("graph", Graph.read_line, Graph.read_reverse_line, Graph.read_first_line)
    service = GraphService(repo)
    console = UI(service)
    console.ui_main()


choice()
