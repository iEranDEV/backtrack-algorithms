import random
import timeit
import hamilton
import euler


# Generowanie grafu acyklicznego skierowanego
def generate_acykliczny_skierowany(n, density):
    graph = {}

    for i in range(0, n):
        graph[i] = [0 for i in range(n)]

    possible_edges = [(i, j) for i in range(0, n) for j in range(i + 1, n)]

    num_edges = n * (n - 1)
    num_edges_wanted = int(num_edges * density)

    if len(possible_edges) >= num_edges_wanted:
        edges_to_add = random.sample(possible_edges, num_edges_wanted)
        for edge in edges_to_add:
            source, target = edge
            graph[source][target] = 1

    return graph


# Generowanie grafu acyklicznego nieskierowanego
def generate_acykliczny_nieskierowany(n, saturation):
    adjacency_matrix = {}
    for i in range(n):
        adjacency_matrix[i] = [0 for _ in range(n)]

    max_edges = (n * (n - 1)) // 2

    num_edges = int(saturation * max_edges)

    possible_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]

    random.shuffle(possible_edges)

    def forms_cycle(adjacency_matrix, u, v):
        n = len(adjacency_matrix)
        visited = [False] * n

        # Perform DFS to check if adding the edge forms a cycle
        stack = [(u, -1)]
        while stack:
            node, parent = stack.pop()
            if visited[node]:
                return True
            visited[node] = True
            for neighbor, connected in enumerate(adjacency_matrix[node]):
                if connected and neighbor != parent:
                    stack.append((neighbor, node))

        return False

    edge_count = 0
    for edge in possible_edges:
        if edge_count >= num_edges:
            break
        u, v = edge
        if not forms_cycle(adjacency_matrix, u, v):
            adjacency_matrix[u][v] = 1
            adjacency_matrix[v][u] = 1
            edge_count += 1

    return adjacency_matrix


# Generowanie grafu cyklicznego skierowanego (Hamilton)
def generate_cykliczny_skierowany_hamilton(n, density):
    adjacency_matrix = {}
    for i in range(n):
        adjacency_matrix[i] = [0 for _ in range(n)]

    for i in range(n):
        adjacency_matrix[i][(i + 1) % n] = 1

    total_edges = n * (n - 1)
    target_edges = int(total_edges * density)

    added_edges = n

    while added_edges < target_edges:
        vertex1, vertex2 = random.sample(range(n), 2)

        if adjacency_matrix[vertex1][vertex2] == 0:
            adjacency_matrix[vertex1][vertex2] = 1
            added_edges += 1

    return adjacency_matrix


# Generowanie grafu cyklicznego nieskierowanego (Hamilton)
def generate_cykliczny_nieskierowany_hamilton(n, density):
    adjacency_matrix = {}
    for i in range(n):
        adjacency_matrix[i] = [0 for _ in range(n)]

    for i in range(n):
        adjacency_matrix[i][(i + 1) % n] = 1
        adjacency_matrix[(i + 1) % n][i] = 1

    total_edges = n * (n - 1) // 2
    target_edges = int(total_edges * density)

    added_edges = n

    while added_edges < target_edges:
        vertex1, vertex2 = random.sample(range(n), 2)

        if adjacency_matrix[vertex1][vertex2] == 0:
            adjacency_matrix[vertex1][vertex2] = 1
            adjacency_matrix[vertex2][vertex1] = 1
            added_edges += 1

    return adjacency_matrix


# Generowanie grafu cyklicznego skierowanego (Euler)
def generate_cykliczny_skierowany_euler(n, saturation):
    adjacency_matrix = {}
    for i in range(n):
        adjacency_matrix[i] = [0 for _ in range(n)]

    for i in range(n):
        adjacency_matrix[i][(i + 1) % n] = 1

    num_edges = int(n * (n - 1) * saturation / 200)
    edges_added = n

    while edges_added < num_edges:
        src = random.randint(0, n - 1)
        dest = random.randint(0, n - 1)

        if dest not in adjacency_matrix[src] and src != dest:
            adjacency_matrix[src][dest] = 1
            edges_added += 1

    return adjacency_matrix


# Generowanie grafu cyklicznego nieskierowanego (Euler)
def generate_cykliczny_nieskierowany_euler(num_nodes, saturation):
    adjacency_matrix = {}
    for i in range(num_nodes):
        adjacency_matrix[i] = [0 for _ in range(num_nodes)]

    for i in range(num_nodes - 1):
        adjacency_matrix[i][i+1] = 1
        adjacency_matrix[i+1][i] = 1
    adjacency_matrix[num_nodes-1][0] = 1
    adjacency_matrix[0][num_nodes-1] = 1

    num_edges_needed = int((saturation / 100) * ((num_nodes * (num_nodes - 1)) / 2) - num_nodes + 1)
    num_edges_generated = 0

    while num_edges_generated < num_edges_needed:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        if node1 != node2 and adjacency_matrix[node1][node2] == 0:
            adjacency_matrix[node1][node2] = 1
            adjacency_matrix[node2][node1] = 1
            num_edges_generated += 1

    return adjacency_matrix


steps = [25] # Dopasuj sobie n
densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
names = ['hamilton', 'euler']

for name in names:
    print(f'ALOGORYTM {name}:')
    for n in steps:
        print(f'    N = {n}:')
        for density in densities:
            print(f'        density = {density}:')
            # Nieskierowany acykliczny
            graph_nieskierowany_acykliczny = generate_acykliczny_nieskierowany(n, density)
            start_1 = timeit.default_timer()
            if name == 'hamilton':
                hamilton.hamilton_adjancency_matrix(graph_nieskierowany_acykliczny)
            else:
                euler.euler_adjacency_matrix(graph_nieskierowany_acykliczny)
            end_1 = timeit.default_timer()
            print('            nieskierowany_acykliczny = {:.10f}'.format(end_1 - start_1))

            # Nieskierowany cykliczny
            if name == 'hamilton':
                graph_nieskierowany_cykliczny = generate_cykliczny_nieskierowany_hamilton(n, density)
                start_2 = timeit.default_timer()
                hamilton.hamilton_adjancency_matrix(graph_nieskierowany_cykliczny)
                end_2 = timeit.default_timer()
                print('            nieskierowany_cykliczny = {:.10f}'.format(end_2 - start_2))
            else:
                graph_nieskierowany_cykliczny = generate_cykliczny_nieskierowany_euler(n, density)
                start_2 = timeit.default_timer()
                euler.euler_adjacency_matrix(graph_nieskierowany_cykliczny)
                end_2 = timeit.default_timer()
                print('            nieskierowany_cykliczny = {:.10f}'.format(end_2 - start_2))

            # Skierowany cykliczny
            if name == 'hamilton':
                graph_skierowany_cykliczny = generate_cykliczny_skierowany_hamilton(n, density)
                start_3 = timeit.default_timer()
                hamilton.hamiltonian_cycle(graph_skierowany_cykliczny)
                end_3 = timeit.default_timer()
                print('            skierowany_cykliczny = {:.10f}'.format(end_3 - start_3))
            else:
                graph_skierowany_cykliczny = generate_cykliczny_skierowany_euler(n, density)
                start_3 = timeit.default_timer()
                euler.znajdz_cykl_eulera_skierowany(graph_skierowany_cykliczny)
                end_3 = timeit.default_timer()
                print('            skierowany_cykliczny = {:.10f}'.format(end_3 - start_3))

            # Skierowany acykliczny
            graph_skierowany_acykliczny = generate_acykliczny_skierowany(n, density)
            if name == 'hamilton':
                """
                start_4 = timeit.default_timer()
                hamilton.hamiltonian_cycle(graph_skierowany_acykliczny)
                end_4 = timeit.default_timer()
                """
                print('            skierowany_acykliczny = ----')
            else:
                start_4 = timeit.default_timer()
                euler.znajdz_cykl_eulera_skierowany(graph_skierowany_acykliczny)
                end_4 = timeit.default_timer()
                print('            skierowany_acykliczny = {:.10f}'.format(end_4 - start_4))
