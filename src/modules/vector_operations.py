
"""
vectors_operations.py
=====================

This module provides basic vector operations using NumPy, including addition, subtraction,
multiplication, division, dot product, and cross product. All functions accept NumPy arrays
or array-like objects and return the result as a NumPy array.

Functions:
    - add_vectors(vec1, vec2): Element-wise addition
    - subtract_vectors(vec1, vec2): Element-wise subtraction
    - multiply_vectors(vec1, vec2): Element-wise multiplication
    - divide_vectors(vec1, vec2): Element-wise division
    - dot_product(vec1, vec2): Dot product
    - cross_product(vec1, vec2): Cross product

Dependencies:
    - numpy
"""

import numpy as np

def add_vectors(vec1, vec2):
    """
    Add two vectors element-wise.

    Parameters:
        vec1 (array-like): First vector.
        vec2 (array-like): Second vector.

    Returns:
        numpy.ndarray: Element-wise sum of vec1 and vec2.
    """
    return np.add(vec1, vec2)

def subtract_vectors(vec1, vec2):
    """
    Subtract the second vector from the first element-wise.

    Parameters:
        vec1 (array-like): First vector.
        vec2 (array-like): Second vector.

    Returns:
        numpy.ndarray: Element-wise difference of vec1 and vec2.
    """
    return np.subtract(vec1, vec2)

def multiply_vectors(vec1, vec2):
    """
    Multiply two vectors element-wise.

    Parameters:
        vec1 (array-like): First vector.
        vec2 (array-like): Second vector.

    Returns:
        numpy.ndarray: Element-wise product of vec1 and vec2.
    """
    return np.multiply(vec1, vec2)

def divide_vectors(vec1, vec2):
    """
    Divide the first vector by the second element-wise.

    Parameters:
        vec1 (array-like): Numerator vector.
        vec2 (array-like): Denominator vector.

    Returns:
        numpy.ndarray: Element-wise division of vec1 by vec2.
    """
    return np.divide(vec1, vec2)

def dot_product(vec1, vec2):
    """
    Compute the dot product of two vectors.

    Parameters:
        vec1 (array-like): First vector.
        vec2 (array-like): Second vector.

    Returns:
        scalar or numpy.ndarray: Dot product of vec1 and vec2.
    """
    return np.dot(vec1, vec2)

def cross_product(vec1, vec2):
    """
    Compute the cross product of two vectors.

    Parameters:
        vec1 (array-like): First vector (must be 3-dimensional).
        vec2 (array-like): Second vector (must be 3-dimensional).

    Returns:
        numpy.ndarray: Cross product of vec1 and vec2.
    """
    return np.cross(vec1, vec2)

def calculate_magnitude(vec):
    """
    Calculate the magnitude (length) of a vector.

    Parameters:
        vec (array-like): Input vector.

    Returns:
        float: Magnitude of the vector.
    """
    return np.linalg.norm(vec, ord = 2)

def calculate_distance(vec1, vec2):
    """
    Calculate the Euclidean distance between two vectors.

    Parameters:
        vec1 (array-like): First vector.
        vec2 (array-like): Second vector.

    Returns:
        float: Euclidean distance between vec1 and vec2.
    """
    return np.linalg.norm(np.subtract(vec1, vec2), ord = 2)

def normalize_vector(vec):
    """
    Normalize a vector to have a magnitude of 1.

    Parameters:
        vec (array-like): Input vector.

    Returns:
        numpy.ndarray: Normalized vector.
    """
    magnitude = calculate_magnitude(vec)
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return np.divide(vec, magnitude)

def amplify_vector(vec, scalar):
    """
    Amplify a vector by a scalar factor.

    Parameters:
        vec (array-like): Input vector.
        scalar (float): Scalar factor to amplify the vector.

    Returns:
        numpy.ndarray: Amplified vector.
    """
    return np.multiply(vec, scalar)

def calculate_manhattan_norm(vec):
    """
    Calculate the norm of a vector.

    Parameters:
        vec (array-like): Input vector.

    Returns:
        float: Norm of the vector.
    """
    return np.linalg.norm(vec, ord = 1)