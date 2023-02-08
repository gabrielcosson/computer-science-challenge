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


def finding_longest_path(available_routes):
    options = [[] for _ in range(len(available_routes))]

    for x in range(len(available_routes) -1, -1, -1):
        #there are 2 possible paths
        if len(available_routes[x]) == 2:
            options[x].append(x)
            if len(options[available_routes[x][0]]) > len(options[available_routes[x][1]]):
                options[x].extend(options[available_routes[x][0]])
            else:
                options[x].extend(options[available_routes[x][1]])

        #there is just 1 path
        elif(len(available_routes[x]) == 1):
            options[x].append(x)
            options[x].extend(options[available_routes[x][0]])
        
        #there is no path
        else:
            options[x].append(x)

    return options


def printing_longest_line(matrix, options):
    longest_line = []
    longest_indexes = max(options, key=len)
    print(longest_indexes)
    
    for i in longest_indexes:
        longest_line.append(matrix[i])
    
    print("Longest Endavans Line Dance is: ", *longest_line)
    print("Length of Path is: ", len(longest_line))


if __name__ == "__main__":
    size, matrix = readFile("DanceFloor06.txt")
    options = finding_longest_path(determining_connections(size, matrix))
    printing_longest_line(matrix, options)