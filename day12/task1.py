import string
import sys
import os

sys.path.append('..')
from utils import print_matrix, print_dict, read_matrix

def add_place(areas, key, place):
    if not key in areas:
        areas[key] = []

    areas[key].append(place)

def find_connected_places(matrix, areas, i, j, value):
    matrix[i][j] = value 
    add_place(areas, value, (i, j))

    if i > 0 and matrix[i-1][j] == value[0]:
        find_connected_places(matrix, areas, i-1, j, value)        
    if i < len(matrix) - 1 and matrix[i+1][j] == value[0]:
        find_connected_places(matrix, areas, i+1, j, value)
    if j > 0 and matrix[i][j-1] == value[0]:
        find_connected_places(matrix, areas, i, j-1, value)
    if j < len(matrix[0]) - 1 and matrix[i][j+1] == value[0]:
        find_connected_places(matrix, areas, i, j+1, value)

def calculate_area1(area):
    result = 0

    for place in area:
        place_perimeter = 4

        if (place[0]-1, place[1]) in area:
            place_perimeter -= 1
        if (place[0], place[1]-1) in area:
            place_perimeter -= 1
        if (place[0]+1, place[1]) in area:
            place_perimeter -= 1
        if (place[0], place[1]+1) in area:
            place_perimeter -= 1

        result += place_perimeter

    return result

def calculate_area(area):
    adj = 0
    for a_i in range(0, len(area)):
        for a_j in range(a_i+1, len(area)):
            if area[a_i][0] == area[a_j][0] and abs(area[a_i][1] - area[a_j][1]) == 1:
                adj += 1
            if area[a_i][1] == area[a_j][1] and abs(area[a_i][0] - area[a_j][0]) == 1:
                adj += 1

    return 4 * len(area) - 2 * adj

# ------------------------------------------------------------------------------------

areas = {}
matrix = read_matrix('input_demo.txt')

print_matrix(matrix)

indexer = {}
for letter in string.ascii_uppercase:
    indexer[letter] = 0

for i, row in enumerate(matrix):
    for j, cell in enumerate(row):
        if len(cell) == 1:
            indexer[cell]+= 1
            cell += f"_{indexer[cell]}"
            find_connected_places(matrix, areas, i, j, cell)
print()
print_matrix(matrix)

print_dict(areas)

result = 0
for area_key in areas:
    perimeter = calculate_area(areas[area_key])
    rank = len(areas[area_key])

    result += perimeter * rank

    # print(area_key, perimeter, rank, perimeter * rank, result)   

print(result)

