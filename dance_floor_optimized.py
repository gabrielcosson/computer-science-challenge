def readFile(fileName):
    matrix = []
    txt = open("./test_files/"+fileName, "r")
    size = int(txt.readline())
    
    for _ in range(size):
        matrix.extend(list(map(int, txt.readline().split())))

    return (size, matrix)


def finding_connections(size, matrix):
    connections = [[] for _ in range(len(matrix))]
    column = 0
    
    for x in range(len(connections)):
        max_column = False

        if column == size-1:
            max_column = True

        #Right path available 
        if (x+1) < len(matrix) and not max_column:
            if abs(matrix[x] - matrix[x+1]) == 1:
                connections[x].append(x+1)
        
        #Down path available
        if (x+size) < len(matrix):
            if abs(matrix[x] - matrix[x+size]) == 1:
                connections[x].append(x+size)
        
        column+=1
        
        if max_column:
            column = 0

    return connections


def longest_path(connections):
    options = [[] for _ in range(len(connections))]

    for x in range(len(connections) -1, -1, -1):
        options[x].append(x)

        #There are two available paths
        if len(connections[x]) == 2:
            if len(options[connections[x][0]]) > len(options[connections[x][1]]):
                options[x].extend(options[connections[x][0]])
            else:
                options[x].extend(options[connections[x][1]])
        
        #There is just one available path
        elif(len(connections[x]) == 1):
            options[x].extend(options[connections[x][0]])

    return max(options, key=len)    


if __name__ == "__main__":
    longest_dancing_line = []
    size, matrix = readFile("DanceFloor07.txt")
    indexes = longest_path(finding_connections(size, matrix))
    
    for i in indexes:
        longest_dancing_line.append(matrix[i])
    
    print("Longest Endavans Line Dance is: ", *longest_dancing_line)
    print("Length of Path is: ", len(longest_dancing_line))