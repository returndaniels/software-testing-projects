import pandas as pd

from pytest import *
from typing import List


def map_true_false(value):
    return "x" if value else " "


def common_vertice(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    if ((x1, y1) == (x3, y3)) or ((x1, y1) == (x4, y4)):
        return True
    if ((x2, y2) == (x3, y3)) or ((x2, y2) == (x4, y4)):
        return True

    return False


def not_common_vertice(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    if ((x1, y1) == (x3, y3)) or ((x1, y1) == (x4, y4)):
        return False
    if ((x2, y2) == (x3, y3)) or ((x2, y2) == (x4, y4)):
        return False

    return True


def is_inside(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    is_x_inside = x3 < x1 < x4 or x3 < x2 < x4
    is_y_inside = y3 < y1 < y4 or y3 < y2 < y4

    return is_x_inside and is_y_inside


def is_not_inside(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    is_x_inside = x3 < x1 < x4 or x3 < x2 < x4
    is_y_inside = y3 < y1 < y4 or y3 < y2 < y4

    return not (is_x_inside and is_y_inside)


def above_line(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    if y3 > y1:
        return True

    return False


def in_line(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    if y3 == y1:
        return True

    return False


def below_line(
    first_retangle_vertices: List[int], second_retangle_vertices: List[int]
) -> bool:
    x1, y1, x2, y2 = first_retangle_vertices
    x3, y3, x4, y4 = second_retangle_vertices

    if y3 < y1:
        return True

    return False


# Testes para a verificacao da logica
def test_vertice_comum():
    assert common_vertice([0, 0, 2, 2], [1, 1, 2, 2]) is True


def test_vertice_is_inside():
    assert is_inside([0, 0, 2, 2], [1, 1, 3, 3]) is True


def test_above_line():
    assert above_line([1, 1, 3, 3], [2, 2, 4, 4]) is True


def test_in_line():
    assert in_line([0, 0, 4, 2], [3, 0, 5, 4]) is True


def test_below_line():
    assert below_line([1, 1, 2, 2], [3, 0, 4, 2]) is True


# Testes para Each Choice


def test_pair_wise():
    expected_result = [
        [True, False, True, False, False, False, True],
        [True, False, False, True, False, True, False],
        [False, True, False, True, False, False, True],
        [False, True, True, False, False, True, False],
        [False, True, False, True, True, False, False],
    ]

    testing_points = [
        ([2, 2, 4, 4], [1, 1, 4, 4]),
        ([2, 2, 4, 4], [1, 2, 4, 4]),
        ([1, 1, 2, 2], [3, 0, 4, 4]),
        ([1, 1, 3, 3], [2, 1, 5, 5]),
        ([1, 1, 3, 3], [4, 2, 5, 4]),
    ]

    testing_functions = [
        common_vertice,
        not_common_vertice,
        is_inside,
        is_not_inside,
        above_line,
        in_line,
        below_line,
    ]

    final_result_vector = []

    for pair_of_points in testing_points:
        result_vector = []
        for func in testing_functions:
            result_vector.append(func(pair_of_points[0], pair_of_points[1]))
        final_result_vector.append(result_vector)

    assert final_result_vector == expected_result


def each_choice():
    testing_points = [
        ([0, 0, 2, 2], [1, 1, 2, 2]),
        ([1, 1, 2, 2], [3, 0, 4, 4]),
    ]
