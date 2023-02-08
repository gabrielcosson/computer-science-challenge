indexes = []

def readFile(filenName):
    matrix = []
    txt = open("./test_files/"+filenName, "r")
    
    for x in txt:
        matrix.append(list(map(int,x.split())))

    matrix.pop(0)
    return matrix
    

def isRightAvailable(matrix, x, y):    
    if (x+1) < len(matrix):
        if abs(matrix[x][y]-matrix[x+1][y]) == 1:
            return True

    return False


def isDownAvailable(matrix, x, y):    
    if (y+1) < len(matrix):
        if abs(matrix[x][y]-matrix[x][y+1]) == 1:
            return True

    return False


def removing_used_items(removing_type, x, y):
    if removing_type == "right":
        if [x+1, y] in indexes:
            indexes.remove([x+1,y])
    elif(removing_type=="down"):
        if [x, y+1] in indexes:
            indexes.remove([x,y+1])


def find_longest_possibility(all_possibilities):
    length = 0
    max_path = 0

    for i in range(len(all_possibilities)):
        if len(all_possibilities[i])>length:
            max_path = i
            length = len(all_possibilities[i])

    return all_possibilities[max_path]
    

def dance_floor(matrix, x, y):
    options = [[]]
    finding_options_algorithm(matrix, x, y, 0, options)
    return options
    

def finding_options_algorithm(matrix, x, y, option_value, options):
    options[option_value].append(matrix[x][y])

    if isDownAvailable(matrix, x, y) and isRightAvailable(matrix, x,y):
        options.append([])
        options.append([])

        option1 = len(options)-2
        option2 = len(options)-1

        for i in options[option_value]:
            options[option1].append(i)
            options[option2].append(i)

        removing_used_items("down", x, y)
        removing_used_items("right", x, y)

        finding_options_algorithm(matrix, x+1, y, option1, options)
        finding_options_algorithm(matrix, x, y+1, option2, options)
        return
    
    if isDownAvailable(matrix, x, y):
        removing_used_items("down", x, y)
        finding_options_algorithm(matrix, x, y+1, option_value, options)
        return
    
    if isRightAvailable(matrix, x, y):
        removing_used_items("right", x, y)
        finding_options_algorithm(matrix, x+1, y, option_value, options)
        return
            
        

if __name__ == "__main__":
    matrix = readFile("DanceFloor07.txt")
    all_possibilities = []

    for y in range(len(matrix)):
        for x in range(len(matrix)):
            indexes.append([x,y])
                
    for value in indexes:     
        options= dance_floor(matrix, value[0], value[1])
        for i in options:
            all_possibilities.append(i)
    

    result = find_longest_possibility(all_possibilities)
    print("Longest Endavans Line Dance is: ", *result)
    print("Length of Path is: ", len(result))