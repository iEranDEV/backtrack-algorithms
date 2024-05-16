def euler_adjacency_matrix(matrix):
    tempMatrix = matrix.copy()
    temp = 0
    n = len(tempMatrix)
    for i in range(n):
        if sum(tempMatrix[i]) % 2 != 0:
            temp = i
            break

    path = []

    def countDFS(v, visited):
        count = 1
        visited[v] = True
        for index, value in enumerate(tempMatrix[v]):
            if value == 1:
                if not visited[index]:
                    count = count + countDFS(index, visited)
        return count

    def isValid(start, end):
        if sum(tempMatrix[start]) == 1:
            return True
        else:
            visited = [False for _ in range(n)]
            count1 = countDFS(start, visited)

            tempMatrix[start][end] = 0
            tempMatrix[end][start] = 0

            visited = [False for _ in range(n)]
            count2 = countDFS(start, visited)

            tempMatrix[start][end] = 1
            tempMatrix[end][start] = 1

            return False if count1 > count2 else True

    def euler_adjacency_matrix_util(start):
        for end, value in enumerate(tempMatrix[start]):
            if value == 1:
                if isValid(start, end):
                    if len(path) == 0 or path[len(path) - 1] != start:
                        path.append(start)
                    path.append(end)
                    tempMatrix[start][end] = 0
                    tempMatrix[end][start] = 0
                    euler_adjacency_matrix_util(end)

    euler_adjacency_matrix_util(temp)
    return path


def znajdz_cykl_eulera_skierowany(macierz_sasiedztwa):
    n = len(macierz_sasiedztwa)
    indegree = [0] * n
    outdegree = [0] * n
    cykl = []

    # Obliczanie stopni wejściowych i wyjściowych dla każdego wierzchołka
    for i in range(n):
        for j in range(n):
            indegree[i] += macierz_sasiedztwa[j][i]
            outdegree[i] += macierz_sasiedztwa[i][j]

    # Sprawdzanie warunku na istnienie cyklu Eulera
    for i in range(n):
        if indegree[i] != outdegree[i]:
            return None  # Nie ma cyklu Eulera

    def dfs(v):
        while outdegree[v] != 0:
            for u in range(n):
                if macierz_sasiedztwa[v][u] > 0:
                    outdegree[v] -= 1
                    macierz_sasiedztwa[v][u] -= 1
                    dfs(u)
        cykl.append(v)

    dfs(0)

    return cykl[::-1]