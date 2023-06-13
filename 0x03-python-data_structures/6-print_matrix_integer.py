#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        s = ""
        for c in row:
            s += str(c) + " "
        print("{}".format(s[:-1]))
