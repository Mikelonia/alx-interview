#!/usr/bin/python3
"""Rotate 2D Matrix 90 Degrees Clockwise."""

def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The input 2D matrix.

    Returns:
        None. The matrix is edited in-place.
    """
  if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    co, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            co += 1
        matrix[-1].append(matrix[r][co])
        if co == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
