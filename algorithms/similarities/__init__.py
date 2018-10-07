def similarity(p1, p2, type=1):
    if type == 1:
        from .euclidean import distance
        return distance(p1, p2)
    elif type == 2:
        from .cosine import distance
        return distance(p1, p2)
    else:
        raise ValueError("This similarity is not defined.")
