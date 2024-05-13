def menu(title, options):
    print("-----------")
    print(title)
    for index, option in enumerate(options):
        print(f'  [{index + 1}.] {option}')
    print("-----------")


def setupAdjacencyMatrix(vertices, connections):
    matrix = {}
    for i in range(0, vertices):
        matrix[i] = [0 for i in range(vertices)]
    for connection in connections:
        matrix[connection[0]][connection[1]] = 1
        matrix[connection[1]][connection[0]] = 1
    return matrix
