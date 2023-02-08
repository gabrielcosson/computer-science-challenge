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
    iterator_per_line = 0
    
    for x in range(len(available_routes)):
        #linear matrix border check
        corner_check = False

        if iterator_per_line == size-1:
            corner_check = True

        #right available 
        if (x+1) < len(matrix) and not corner_check:
            if abs(matrix[x] - matrix[x+1]) == 1:
                available_routes[x].append(x+1)
        
        #down available
        if (x+size) < len(matrix):
            if abs(matrix[x] - matrix[x+size]) == 1:
                available_routes[x].append(x+size)
        
        iterator_per_line+=1
        if corner_check:
            iterator_per_line = 0

    return available_routes


if __name__ == "__main__":
    size, matrix = readFile("DanceFloor05.txt")
    options = determining_connections(size, matrix)
    print(options)
