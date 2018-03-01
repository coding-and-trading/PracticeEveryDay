def minkowskiDist(v1, v2, p):
    if len(v1) is not len(v2):
        raise ValueError("Two vector must have same elements.")

    each_dist = [abs(v1[i] - v2[i])**p for i in range(len(v1))]
    return sum(each_dist)**(1/p)
