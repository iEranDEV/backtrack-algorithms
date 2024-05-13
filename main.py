import utils
import hamilton
import euler
import sys

sys.setrecursionlimit(10**6)

matrix = {}
vertices = 0
connections = []

utils.menu("Jak chcesz przedstawić graf?", ["Macierz sąsiedztwa", "Macierz grafu"])
structureType = int(input("Podaj typ reprezentacji maszynowej: "))

utils.menu("Jak chcesz wczytać dane?", ["Z klawiatury", "Z pliku input.txt"])
inputType = int(input("Podaj typ wprowadzenia danych: "))

# Wczytanie krawędzi
if inputType == 1:
    vertices = int(input("Podaj ilość wierzchołków: "))
    print("Podaj połączenia (np. 1 3). Zakończ wpisując 0")
    while True:
        temp = input("")
        if temp == "0":
            break
        connections.append(list(map(int, temp.split())))
elif inputType == 2:
    readFile = open("input.txt", "r")
    for index, line in enumerate(readFile):
        if index == 0:
            vertices, _ = list(map(int, line.rstrip('\n').split()))
        else:
            connections.append(list(map(int, line.rstrip('\n').split())))
    readFile.close()

# Utworzenie grafu
if structureType == 1:
    matrix = utils.setupAdjacencyMatrix(vertices, connections)
elif structureType == 2:
    print('2')

utils.menu("Jakiego algorytmu chcesz użyć?", ["Roberta-Floresa (cykl Hamiltona)", "Fleury'ego (cykl Eulera)"])
algType = int(input("Podaj wybrany algorytm: "))

# TODO: Wykonania

if algType == 1:
    if structureType == 1:
        value, path = hamilton.hamilton_adjancency_matrix(matrix)
        if value:
            print(f'Cykl Hamiltona = {path}')
        else:
            print("Nie istnieje cykl Hamiltona w tym grafie.")

elif algType == 2:
    if structureType == 1:
        path = euler.euler_adjacency_matrix(matrix)
        if len(path) > 0:
            print(f'Cykl Eulera = {path}')
        else:
            print("Nie istnieje cykl Hamiltona w tym grafie.")
