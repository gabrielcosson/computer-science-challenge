import sys


def readFile(fileName):
    matrix = []
    txt = open("./test_files/"+fileName, "r")
    
    for x in txt:
        for value in list(map(int,x.split())):
            matrix.append(value)

    size = matrix.pop(0)
    return (size, matrix)


def determining_connections(size, matrix):
    available_routes = [[] for _ in range(len(matrix))]
    for x in range(len(available_routes)):
        #right available 
        if (x+1) < len(matrix):
            if abs(matrix[x] - matrix[x+1]) == 1:
                available_routes[x].append(x+1)
        #down available
        if (x+size) < len(matrix):
            if abs(matrix[x] - matrix[x+size]) == 1:
                available_routes[x].append(x+size)

    return available_routes



if __name__ == "__main__":
    size, matrix = readFile("DanceFloor01.txt")
    print(determining_connections(size, matrix))
