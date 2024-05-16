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


# BLE BLE BLE
def is_valid_next_vertex(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True


def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(len(graph)):
        if is_valid_next_vertex(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False


def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0

    if not hamiltonian_cycle_util(graph, path, 1):
        return False

    return True
