"""
Aлгоритм работы :
1) Находим рандомную точку на карте
2) Получаем её координаты, запоминаем в отдельную переменную
3) Рандомно выбираем матрицу с озером
4) Ищем диагонали матрицы
5) Расширяем область зоны матрицы (ищем диагональ, ( матрица должна быть квадратная)
делаем срез вправо, потом срез вниз, влево и срез вверх)  тут получается большой квадрат, тоесть область видимости 
6) Прогоняемся по этой области циклом, если находим (20), то переходим к пункту 1 , иначе, проганяемся ещё раз и заполняем координаты значениями из нашей  матрицы с водой
7) Повторяем итерации, пока не заполним опредёленный процент от озера

e.g 
# 1,2) point = [20, 20]     (point = [randint(0,999), randint(0,999)]
# 3) chosen matrix = [[0, 20, 0],
                     [20, 20, 20],
                     [0, 20, 0]]     так как её длина равна 3х3 , желаемый срез получается  -4  + длина рядка нашей матрицы + 4  тоесть диапазон точек      [i-4][j-4]
                     
The random array of dots is [150, 150]

# ot tochki 16,16  do tochki 24,24

# 16 16,  16 17,   16 18,  16 19,   16 20,   16 21,   16 22, 16 23                     # 1 1, 1 2, 1,3
# 17 16,  17 17,   17 18,  17 19,   17 20,   17 21,   17 22  17 23                     # 2 1, 2 2, 2,3
# 18,16,  18 17,   18 18,  18 19,   18 20,   18 21,   18 22  18 23

from random import choice, randint
from typing import List

#list_of_all_matrix = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7]  # creating list of all matrixes
import numpy as np

"""
from random import randint
from typing import List


def get_random_points():
    """
    The function looks for a random point and forms a list from them
    :return: the points array       e.g (points[11,11])
    """
    #random_point = randint(7, 993)       # within special area
    random_point1 = randint(7, 993)       # within special area
    random_point2 = randint(7, 993)       # within special area

    points = [random_point1] + [random_point2]  # get the coords of this dot on the map
    return points

def find_coverage_area(points: List):
    """
    The function returns a coverage area for all matrix
    :param points: List of coords
    :return: the row from and to it also works for the columns  for insta
    """

    row_from = points[0] - 4  # проверка на выход за карту
    row_to = points[1] + 4
    return row_from, row_to if row_from>0 and row_to<1000 else [0,0]

   # return row_from, row_to if row_from>0 and row_to<1000 else [0,0]


def generate_map_matrix():
    #return np.zeros((20,20), dtype = int)
    return np.zeros((1000,1000), dtype = int)
     #return [[0 for __ in range(20)] for _ in range(20)] # [
    # return [[0 for __ in range(1000)] for _ in range(1000)]  # generate the matrix


def make_world_file(matrix):
    with open("World.txt", 'w', encoding='utf-8') as input_file:
        input_file.write(str(matrix))
        # input_file.write(str(np.array(matrix)) + '\n')
        # input_file.write("=" * 20 + '\n')


