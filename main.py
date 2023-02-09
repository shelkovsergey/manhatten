# calculate3
# create function to calculate Manhattan distance
import numpy as np


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


centr1 = [2.33, 4.33]
centr2 = [3.33, 2]

const = [2.5, 0.5]
# define vectors
arr = [[1, 4], [2, 2], [2, 5], [3, 3], [4, 4], [5, 1], [100, 100], [100, 100]]
literal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("c1 c2")
for i in range(len(arr)):
    print(literal[i], manhattan(centr1, arr[i]), manhattan(centr2, arr[i]))
print("__________________________________________")
print("const")
for i in range(len(arr)):
    print(literal[i], manhattan(const, arr[i]))
print("__________________________________________")

buff = [0] * 8
buff2 = [0] * 8
buff3 = [0] * 8
buff4 = [0] * 8
buff5 = [0] * 8
buff6 = [0] * 8
buff7 = [0] * 8
buff8 = [0] * 8

for i in range(len(arr)):
    buff[i] = manhattan(arr[0], arr[i])
    buff2[i] = manhattan(arr[1], arr[i])
    buff2[0] = 0
    buff3[i] = manhattan(arr[2], arr[i])
    buff3[0] = 0
    buff3[1] = 0
    buff4[i] = manhattan(arr[3], arr[i])
    buff4[0] = 0
    buff4[1] = 0
    buff4[2] = 0
    buff5[i] = manhattan(arr[4], arr[i])
    buff5[0] = 0
    buff5[1] = 0
    buff5[2] = 0
    buff5[3] = 0
    buff6[i] = manhattan(arr[5], arr[i])
    buff6[0] = 0
    buff6[1] = 0
    buff6[2] = 0
    buff6[3] = 0
    buff6[4] = 0
    buff7[i] = manhattan(arr[6], arr[i])
    buff7[0] = 0
    buff7[1] = 0
    buff7[2] = 0
    buff7[3] = 0
    buff7[4] = 0
    buff7[5] = 0
    buff8[i] = manhattan(arr[7], arr[i])
    buff8[0] = 0
    buff8[1] = 0
    buff8[2] = 0
    buff8[3] = 0
    buff8[4] = 0
    buff8[5] = 0
    buff8[6] = 0

# calculate Manhattan distance between vectors
matrix = ([buff, buff2, buff3, buff4, buff5, buff6, buff7, buff8])
n = np.array(literal)
print('', matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print(matrix[4])
print(matrix[5])
print(matrix[6])
print(matrix[7])
print("__________________________________________")

print("  ", n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7])
for i in range(8):
    print(literal[i], manhattan(arr[0], arr[i]), manhattan(arr[1], arr[i]),
          manhattan(arr[2], arr[i]), manhattan(arr[3], arr[i]),
          manhattan(arr[4], arr[i]), manhattan(arr[5], arr[i]),
          manhattan(arr[6], arr[i]), manhattan(arr[7], arr[i]))
