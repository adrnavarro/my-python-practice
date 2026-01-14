"""
_matrix_operations.py
=============

This module provides basic vector operations using NumPy, including addition, subtraction,
multiplication, division, dot product, and cross product. All functions accept NumPy arrays
or array-like objects and return the result as a NumPy array.

Functions:
	- determine_matrix_shape(matrix): Get the shape of a matrix
    - add_matrices(mat1, mat2): Element-wise addition
    - subtract_matrices(mat1, mat2): Element-wise subtraction
    - calculate_determinant(mat): Determinant of a matrix
    - invert_matrix(mat): Inverse of a matrix

Dependencies:
	- numpy
"""

import numpy as np

def determine_matrix_shape(matrix):
    """
    Determine the shape of a matrix.

    Parameters:
        matrix (array-like): Input matrix.

    Returns:
        tuple: Shape of the matrix.
    """
    mat = np.array(matrix)
    return mat.shape

def add_matrices(mat1, mat2):
    """
    Add two matrices element-wise.

    Parameters:
        mat1 (array-like): First matrix.
        mat2 (array-like): Second matrix.

    Returns:
        numpy.ndarray: Element-wise sum of mat1 and mat2.
    """
    return np.add(mat1, mat2)

def subtract_matrices(mat1, mat2):
    """
    Subtract the second matrix from the first element-wise.

    Parameters:
        mat1 (array-like): First matrix.
        mat2 (array-like): Second matrix.

    Returns:
        numpy.ndarray: Element-wise difference of mat1 and mat2.
    """
    return np.subtract(mat1, mat2)

def calculate_determinant(mat):
    """
    Calculate the determinant of a square matrix.

    Parameters:
        mat (array-like): Input square matrix.

    Returns:
        float: Determinant of the matrix.
    """
    return np.linalg.det(mat)

def invert_matrix(mat):
    """
    Calculate the inverse of a square matrix.

    Parameters:
        mat (array-like): Input square matrix.

    Returns:
        numpy.ndarray: Inverse of the matrix.
    """
    return np.linalg.inv(mat)