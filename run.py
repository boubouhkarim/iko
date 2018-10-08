# import scv

# import knn.descent

# import viz

# data = csv('file.csv')

# knn = knn_descent(data, k=10)

# viz(knn)

from data.csv_reader import reader
from algorithms.knn import knn_brute_force
from algorithms.knn import knn_descent

k = 3
graph = reader("/home/karim/Workspace/github.com/me/iko/datasets/data.csv")

knn_graph = knn_descent.get_knn(graph, k)
knn_descent.print_knn(knn_graph)

# knn_graph = knn_brute_force.get_knn(graph, k)
# knn_brute_force.print_knn(knn_graph)