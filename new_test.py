# from random import randint, choice
# from typing import List
#
#
# def generate_water_matrixes():
#     """
#     Water matrixes are generated
#     :return: the array with randomly generated sizes of matrixes
#     """
#     # the 45% of the map must be covered with water    so it is 450x450 size        # 202500
#     # Water.set_value_of_coverage()
#     sum_of_matrix_sizes = 0
#     water_matrix = []
#     while sum_of_matrix_sizes <= 450 * 450:
#         x, y = randint(6, 14), randint(6, 14)  # generated random blocks n x m
#         sum_of_matrix_sizes += x * y
#         if sum_of_matrix_sizes < 450 * 450:  # # 202500
#             water_matrix.append([x, y])  # find square of the generated
#     return water_matrix
#
#
# print(generate_water_matrixes())
# WORLD_MAP_SIZE = 1000 * 1000
#
# import numpy as np
#
#
# def filter_data(coords:List, matrix_coords:List):
#     # the function checks inital value and max value of
#     return coords[0] < matrix_coords[0] and coords[1] < matrix_coords[1]
#
# def get_possible(center: List, matrix_coords=[3,3]):
#     """
#     The function evaluates and validates possible coords
#     :param center: the central coords x,y
#     :param matrix_coords: coords of the matrix n x m
#     :return: The possible options
#     #TODO rewrite the whole code into numpy
#     """
#     # how to calculate diagonals
#     x, z = matrix_coords[0], matrix_coords[1]       # unpacking values in order to validate
#     # границы должны быть  (размер матрицы - 1)   № 0 1 2 3 4 5
#     possible_coords = [[center[0] - 1, center[1] - 1],
#                        [center[0] - 1, center[1]],
#                        [center[0] - 1, center[1] + 1],  # it is the first row
#                        [center[0], center[1] - 1],
#                        [center[0], center[1] + 1],  # it is the second row
#                        [center[0] + 1, center[1] - 1],
#                        [center[0] + 1, center[1]],
#                        [center[0] + 1, center[1] + 1]]  # it is the third row
#     counter = 0
#
#     return possible_coords
#
#
# # def generate_lake(lake_array: List, square_percentage: float):
# #     """
# #     Lake array  e.g 3*4
# #     :param lake_array: random array with the sizes of lake
# #     :param square_percentage: the resulted we want to draw of the square of the lake in %
# #     :return:
# #     """
# #     x, z = lake_array[0], lake_array[1]  # check
# #     water_matrix = [[0 for __ in range(x)] for _ in range(z)]  # generate the matrix
# #     print(f"The initial matrix with 0 size is {x} x {z}")
# #     center_x, center_y = x // 2, z // 2  # find x center coord , and z center coord inside the matrix
# #     water_matrix[center_x][center_y] = 1  # define the coord that it is a part of the lake
# #     print(np.array(water_matrix))
# #     print(f"Central coord x: {center_x}")
# #     print(f"Central coord y: {center_y}")
# #     center = [center_x, center_y]  # here is the center array
# #     possible = get_possible(center)
# #     print(np.array(possible))
# #     for i in range(len(possible)):
# #         print(possible[i])
#
#
# generate_lake([6, 6], 10)
# """
# The function receive x,y and returns the matrix with x,y covered with 0
# """
from math import floor

matrix1 = [[20, 20, 20, 20],
           [20, 20, 20, 20],
           [20, 20, 20, 20],
           [0, 20, 20, 0]]

matrix2 = [[0, 20, 0],
           [20, 20, 20],
           [0, 20, 0]]

matrix3 = [[0, 20, 20, 20, 0],
           [20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20],
           [0, 20, 20, 20, 0], ]

matrix4 = [[20, 20, 20],
           [20, 20, 20],
           [20, 20, 20]]

matrix5 = [[20, 20, 0],
           [20, 20, 20],
           [0, 20, 20]]

matrix6 = [[0, 0, 20, 20, 20, 0, 0],
           [0, 0, 20, 20, 20, 20, 0],
           [0, 20, 20, 20, 20, 20, 20],
           [0, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],
           [0, 20, 20, 20, 20, 20, 20],]

matrix7 = [[0, 20, 20, 20, 0, 0, 0],
           [0, 20, 20, 20, 20, 0, 0],
           [0, 20, 20, 20, 20, 20, 0],
           [0, 20, 20, 20, 20, 20, 0],
           [20, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],
           [20, 20, 20, 20, 20, 20, 20],]



def find_matrix_center(matrix):
    """
    The function gets the coords of matrix
    :param matrix: MATRIX to find center
    :return:
    """
    center = [floor(len(matrix[0])/2),floor(len(matrix)/2)]
    return center

list_of_all_matrix = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7]  # [[2, 2], [1, 1], [2, 2], [1, 1], [1, 1], [3, 3], [3, 3]]


centers = []
for i in range(len(list_of_all_matrix)):
    centers.append(find_matrix_center(list_of_all_matrix[i]))

print(centers)