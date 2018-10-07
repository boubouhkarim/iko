class Node(object):
    id = 0
    neighbours = {}
    reverse = []
    profil = []
    general_neighbours = []

    def __init__(self, id, profil):
        self.id = id
        self.profil = profil

    def __str__(self):
        return f"Node[{self.id}]"

    def add_neighbours(self, node, d):
        self.neighbours.update({node: d})

    def set_neighbours_revers(self):
        for n, d in self.neighbours:
            n.add_revers(self)

    def add_revers(self, revers_node):
        self.reverse.add(revers_node);

    def set_general_neighbours(self):
        self.general_neighbours = list(set(list(self.neighbours.keys()) + self.reverse))

    def get_farest_neighbour(self):
        # dict(sorted(words.items(), key=lambda x: x[1]))
        # sorted(stats, key=(lambda key: stats[key]), reverse=True)
        # max(stats.items(), key=lambda x: x[1])
        return max(self.neighbours, key=self.neighbours.get)


if __name__ == '__main__':
    # node = Node()
    print(__name__)
