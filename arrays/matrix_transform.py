""" Matrix transformations """

from typing import List


def matrix_transpose(matrix: List[List]) -> List[List]:
    """
    The transpose of a matrix is the matrix flipped over it's main diagonal,
    switching the row and column indices of the matrix
    """
    # return [list(row) for row in zip(*matrix)]
    return list(map(list, zip(*matrix)))


def matrix_flip_horizontal(matrix: List[List]) -> List[List]:
    """ Flip matrix along its horizontal axis """
    # return list(reversed(matrix))
    return matrix[::-1]


def matrix_flip_vertical(matrix: List[List]) -> List[List]:
    """ Flip matrix along its vertical axis """
    # return [list(reversed(row)) for row in matrix]
    return [row[::-1] for row in matrix]


def matrix_rotate_right(matrix: List[List]) -> List[List]:
    """ Rotate Matrix on 90 degrees clockwise (to the right) """
    # return [list(reversed(row)) for row in zip(*matrix)]
    # return [list(row) for row in zip(*reversed(matrix))]
    # return list(map(list, zip(*reversed(matrix))))
    return list(map(list, zip(*matrix[::-1])))


def matrix_rotate_left(matrix: List[List]) -> List[List]:
    """ Rotate Matrix on 90 degrees counterclockwise (to the left) """
    # return [list(row) for row in zip(*matrix)][::-1]
    return list(map(list, zip(*matrix)))[::-1]


example_matrix_1 = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
]

example_matrix_2 = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
]

print('matrix_transpose():')
print(matrix_transpose(example_matrix_1))
print(matrix_transpose(example_matrix_2))
print()
print('matrix_flip_horizontal():')
print(matrix_flip_horizontal(example_matrix_1))
print(matrix_flip_horizontal(example_matrix_2))
print()
print('matrix_flip_vertical():')
print(matrix_flip_vertical(example_matrix_1))
print(matrix_flip_vertical(example_matrix_2))
print()
print('matrix_rotate_right():')
print(matrix_rotate_right(example_matrix_1))
print(matrix_rotate_right(example_matrix_2))
print()
print('matrix_rotate_left():')
print(matrix_rotate_left(example_matrix_1))
print(matrix_rotate_left(example_matrix_2))
print()
