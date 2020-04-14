# Write a function that takes a 2D binary array and returns 
# the number of 1 islands. An island consists of 1s that are 
# connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

import random

def generate_island_matrix(width, height, density):
    matrix = []
    for h in range(height):
        matrix.append([0] * width)
    for x in range(width):
        for y in range(height):
            print(random.random() < density)
            if random.random() < density:
                matrix[y][x] = 1
    return matrix
    
# generate_island_matrix(10, 10, 0.5)