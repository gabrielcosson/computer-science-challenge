def readFile(fileName):
    matrix = []
    txt = open("./test_files/"+fileName, "r")
    size = int(txt.readline())
    
    for _ in range(size):
        matrix.extend(list(map(int, txt.readline().split())))

    return (size, matrix)


def longest_path(size, matrix):
    options = [[] for _ in range(len(matrix))]
    column = size

    for x in range(len(options) -1, -1, -1):
        options[x].append(x)
        right_extension = []
        down_extension = []

        #Right Path Available
        if column!=size and (x+1) < len(matrix) and abs(matrix[x] - matrix[x+1]) == 1:
            right_extension = options[x+1]

        #Down Path Available
        if (x+size) < len(matrix) and abs(matrix[x] - matrix[x+size]) == 1:
            down_extension = options[x+size]

        #Extending the Longest Path
        if len(right_extension) > len(down_extension):
            options[x].extend(right_extension)
        else:
            options[x].extend(down_extension)

        column = column - 1

        if column == 0:
            column = size

        
    return max(options, key=len)    


if __name__ == "__main__":
    longest_dancing_line = []
    size, matrix = readFile("DanceFloor07.txt")
    indexes = longest_path(size, matrix)

    for i in indexes:
        longest_dancing_line.append(matrix[i])
    
    print("Longest Endavans Line Dance is: ", *longest_dancing_line)
    print("Length of Path is: ", len(longest_dancing_line))