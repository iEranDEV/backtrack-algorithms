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
                    # print(f'{start} -> {end} ', end=" "),
                    if len(path) == 0 or path[len(path) - 1] != start:
                        path.append(start)
                    path.append(end)
                    tempMatrix[start][end] = 0
                    tempMatrix[end][start] = 0
                    euler_adjacency_matrix_util(end)

    euler_adjacency_matrix_util(temp)
    return path
