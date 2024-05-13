def hamilton_adjancency_matrix(matrix):
    def is_valid(v, k, path):
        return matrix[path[k - 1]][v] == 1 and v not in path

    def hamilton_adjacency_util(path, pos):
        if pos == len(matrix):
            return matrix[path[pos - 1]][path[0]] == 1

        for v in range(1, len(matrix)):
            if is_valid(v, pos, path):
                path[pos] = v
                if hamilton_adjacency_util(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    path = [-1 for _ in range(len(matrix))]
    path[0] = 0

    return [hamilton_adjacency_util(path, 1), path]
