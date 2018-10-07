from collections import OrderedDict
from itertools import islice

from ..similarities import similarity

def get_knn(graph, k, type=1):
    matrix = {}
    for current_node in graph:
        sim_matrix = {}
        for node in graph:
            if current_node.id != node.id:
                sim_matrix.update({node: similarity(current_node.profil, node.profil, type)})
                s = dict(islice(OrderedDict(sorted(sim_matrix.items(), key=(lambda x: x[1]))).items(), k))
                matrix.update({current_node: s})

    return  matrix

def print_knn(graph):
    for node, neighbours in graph.items():
        print(node)
        for k, v in neighbours.items():
            print(f"    {k} : {v}")
