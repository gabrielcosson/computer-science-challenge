import sys

def readFile():
    matrix = []
    txt = open("./test_files/DanceFloor01.txt", "r")
    
    for x in txt:
        matrix.append(list(map(int,x.split())))

    matrix.pop(0)
    return matrix
    
    
if __name__ == "__main__":
    matrix = readFile()
    print(matrix)