import sys


def readFile(fileName):
    matrix = []
    txt = open("./test_files/"+fileName, "r")
    
    for x in txt:
        for value in list(map(int,x.split())):
            matrix.append(value)

    size = matrix.pop(0)
    return (size, matrix)





if __name__ == "__main__":
    size, matrix = readFile("DanceFloor01.txt")
    print(matrix)