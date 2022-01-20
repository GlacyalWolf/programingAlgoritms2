from re import sub
from easyinput import read
import sys

row, col = read(int, int)
matrix = []
submatrix = []
for x in range(row):
    for i in range(col):
        submatrix.append(read(int))
    matrix.append(submatrix)
    submatrix = []
 