import sys

if __name__ == "__main__":
    rows = int(sys.stdin.readline())

    matrix = []
    for i in range(rows):
        row = list(map(int,sys.stdin.readline().split()))
        matrix.append(row)
    print(matrix)