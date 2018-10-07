from collections import OrderedDict
from itertools import islice
from random import sample

from ..similarities import similarity

def _sample(graph, k):


# work in progress
def get_knn(graph, k, type=1): 

    nodes = sample(graph, k)

    c = 0

    while True:
        # reverse calcutation for all the node
        _revers(nodes)
        for node in nodes:
            node.set_general_neighbours()

        c = 0

        for node in nodes:
            for u in node.general_neighbours:
                if u



        if (u1.getGeneralNeighbours().contains(v)) u1.getGeneralNeighbours().remove(v);



        #     for (Node v : nodes) {
        #         for (Node u1 : v.getGeneralNeighbours()) {
        #             if (u1.getGeneralNeighbours().contains(v)) u1.getGeneralNeighbours().remove(v);
        #             for (Node u2 : u1.getGeneralNeighbours()) {
        #                 // looking for neighbours in my neighbours neighbours
        #                 Double l = similarity(type, v.getProfile(), u2.getProfile());
        #                 c += UpdateNN(v, u2, l);
        #             }
        #         }
        #     }
        # } while (c != 0);



    matrix = {}
    for current_node in graph:
        sim_matrix = {}
        for node in graph:
            if current_node.id != node.id:
                sim_matrix.update({node: similarity(current_node.profil, node.profil, type)})
                s = dict(islice(OrderedDict(sorted(sim_matrix.items(), key=(lambda x: x[1]))).items(), k))
                matrix.update({current_node: s})

    return  matrix


def _revers(nodes):
    pass

def print_knn(graph):
    for node, neighbours in graph.items():
        print(node)
        for k, v in neighbours.items():
            print(f"    {k} : {v}")
