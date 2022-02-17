import random
from random import choice
from  math import floor
import numpy as np

import adasd
from ready_program import generate_map_matrix, find_coverage_area, get_random_points , make_world_file

world_map = generate_map_matrix()       # creating map 1000 x 1000
print(f"The world map is: \n  {np.array(world_map)}")


"""
План работы :

1) Сгенерировать карту воды,            done()
2) Попробовать визуализировать массив воды в пикселях  done()
3) Передать Дане в формате json (тип озера, его центральные координаты, форма озера)  
"""


matrix1 = [[20, 20, 20, 20],
           [20, 20, 20, 20],
           [20, 20, 69, 20],
           [0, 20, 20, 0]]

matrix2 = [[0, 20, 0],
           [20, 69, 20],
           [0, 20, 0]]

matrix3 = [[0, 20, 20, 20, 0],
           [20, 20, 20, 20, 20],
           [20, 20, 69, 20, 20],
           [20, 20, 20, 20, 20],
           [0, 20, 20, 20, 0], ]

matrix4 = [[20, 20, 20],
           [20, 69, 20],
           [20, 20, 20]]

matrix5 = [[20, 20, 0],
           [20, 69, 20],
           [0, 20, 20]]

matrix6 = [[0, 0, 20, 20, 20, 0, 0],
           [0, 0, 20, 20, 20, 20, 0],
           [0, 20, 20, 20, 20, 20, 20],
           [0, 20, 20, 69, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],
           [0, 20, 20, 20, 20, 20, 20],]

matrix7 = [[0, 20, 20, 20, 0, 0, 0],
           [0, 20, 20, 20, 20, 0, 0],
           [0, 20, 20, 20, 20, 20, 0],
           [0, 20, 20, 69, 20, 20, 0],
           [20, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],]


list_of_all_matrix = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7]  # creating list of all matrixes


def choose_matrix():
    # the function gets random matrix and returns it
    return choice(list_of_all_matrix)


def validate_coords(row_from, row_to):
    # the function which validates the coords of the map range
    return False if row_from < 0 or row_to > 1000 else True



def find_matrix_center(matrix):
    """
    The function gets the coords of matrix
    :param matrix: MATRIX to find center
    :return: center of the matrix
    """
    center = [floor(len(matrix[0])/2), floor(len(matrix)/2)]
    return center

def check_lake_presence(column_from,column_to):
    """
    The function checks the presence of the lakes
    :param coord: row_from, row_to represented in coords
    :return: bool (whether the area is appropriate to make a lake)
    """
    for i in range(column_from):
        for j in range(column_to):
            if world_map[i][j] == 20 or world_map[i][j] == 69:
                return False
            else:
                return True


def find_center_of_the_lake_on_the_map(coords):
    #coords = find_matrix_center()
    pass

def generate_lakes():
    chosen_matrix = choose_matrix()
    matrix_width, matrix_length = np.shape(chosen_matrix)
    print("Width: ", matrix_width, "Length: ", matrix_length)
    print("Chosen matrix")
    print(np.array(chosen_matrix))
    random_points = get_random_points()
    x, z = random_points        # тут мы получаем значения с какой точки , до куда сделать срез
    print("Random coords are:", random_points)
    row_from, row_to = find_coverage_area(random_points)
    column_from, column_to = find_coverage_area(random_points)
    print(f"The coords to_check are: from {column_from} to {column_to}")
    lake_center = (find_matrix_center(chosen_matrix))
    print(f"The center of the lake is: {lake_center}")
    flag = check_lake_presence(column_from,column_to) and validate_coords(row_from, row_to)  # проверка не выходим ли мы за границу карты или же не находим озеро в квадрате

    if flag:
        world_map[x:x + matrix_width, z:z + matrix_length] = chosen_matrix

for i in range(600):
    generate_lakes()
    #print(world_map)


def draw_the_map(world_map):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(50,50))
    plt.imshow(world_map)
    plt.show()
    #plt.savefig('saved_figure-1000dpi.png', dpi=1000)



def make_map_from_np_array(world_map):
    # the function returns normal array from 2-d list
    return world_map.tolist()

world_map = make_map_from_np_array(world_map)

print(world_map)
draw_the_map(world_map)

#print(np.array(world_map))



