import sys

def readFile():
    matrix = []
    txt = open("./test_files/DanceFloor01.txt", "r")
    
    for x in txt:
        matrix.append(list(map(int,x.split())))

    matrix.pop(0)
    return matrix
    

def isDownAvailable(matrix, x, y):    
    if (x+1) < len(matrix):
        if abs(matrix[x][y]-matrix[x+1][y]) == 1:
            return True

    return False


def isRightAvailable(matrix, x, y):    
    if (y+1) < len(matrix):
        if abs(matrix[x][y]-matrix[x][y+1]) == 1:
            return True

    return False


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

        finding_options_algorithm(matrix, x+1, y, option1, options)
        finding_options_algorithm(matrix, x, y+1, option2, options)
        return
    
    if isDownAvailable(matrix, x, y):
        finding_options_algorithm(matrix, x+1, y, option_value, options)
        return
    
    if isRightAvailable(matrix, x, y):
        finding_options_algorithm(matrix, x, y+1, option_value, options)
        return
    
    return
            
        

if __name__ == "__main__":
    matrix = readFile()
    all_possibilities = []

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            options= dance_floor(matrix, x,y)
            for i in options:
                all_possibilities.append(i)
    
    print("Longest Endavans Line Dance is: ",*find_longest_possibility(all_possibilities))
    print("Length of Path is: ",len(find_longest_possibility(all_possibilities)))