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
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
