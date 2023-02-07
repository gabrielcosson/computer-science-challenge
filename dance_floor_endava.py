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
    
    
def dance_floor(matrix, x, y):
    sequence = []
    dance_floor_algorithm(matrix, x, y, sequence)
    return sequence


def dance_floor_algorithm(matrix, x, y, sequence):
    sequence.append(matrix[x][y])
    if not isDownAvailable(matrix, x, y) and not isRightAvailable(matrix, x,y):
        return
    
    if isDownAvailable(matrix, x, y):
        dance_floor_algorithm(matrix, x+1, y, sequence)
        return
    
    if isRightAvailable(matrix, x, y):
        dance_floor_algorithm(matrix, x, y+1, sequence)
        return
            
        


if __name__ == "__main__":
    matrix = readFile()
    print(dance_floor(matrix, 1,1))