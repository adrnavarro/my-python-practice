"""
vector_app.py
=============

A command-line application to perform vector operations using the functions from vectors_operations.py.

Usage Example:
--------------
To start the script, activate your virtual environment and run:

    python3 -m scripts.vector_app

or (from the src directory):

    python3 -m scripts.vector_app

To stop the script, select the 'Exit' option from the menu or press Ctrl+C.
"""

import sys
import numpy as np
from modules.vetor_operations import (
    add_vectors, subtract_vectors, multiply_vectors, divide_vectors,
    dot_product, cross_product, calculate_magnitude, calculate_distance,
    normalize_vector, amplify_vector, calculate_manhattan_norm
)

def get_vector(prompt):
    raw = input(prompt)
    try:
        vec = np.array([float(x) for x in raw.strip().split()])
        return vec
    except Exception:
        print("Invalid input. Please enter numbers separated by spaces.")
        return get_vector(prompt)

def get_scalar(prompt):
    raw = input(prompt)
    try:
        return float(raw.strip())
    except Exception:
        print("Invalid input. Please enter a number.")
        return get_scalar(prompt)

def main():
    menu = [
        "Add two vectors (e.g. 1 2 3)",
        "Subtract two vectors (e.g. 1 2 3)",
        "Multiply two vectors element-wise (e.g. 1 2 3)",
        "Divide two vectors element-wise (e.g. 1 2 3)",
        "Dot product of two vectors (e.g. 1 2 3)",
        "Cross product of two 3D vectors (e.g. 1 2 3)",
        "Calculate magnitude of a vector (e.g. 1 2 3)",
        "Calculate distance between two vectors (e.g. 1 2 3)",
        "Normalize a vector (e.g. 1 2 3)",
        "Amplify a vector by a scalar (e.g. vector: 1 2 3, scalar: 2.5)",
        "Calculate Manhattan norm (L1) of a vector (e.g. 1 2 3)",
        "Exit"
    ]
    while True:
        print("\nVector Operations Menu:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")
        try:
            choice = int(input("Select an option (1-12): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", add_vectors(v1, v2))
        elif choice == 2:
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", subtract_vectors(v1, v2))
        elif choice == 3:
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", multiply_vectors(v1, v2))
        elif choice == 4:
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", divide_vectors(v1, v2))
        elif choice == 5:
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", dot_product(v1, v2))
        elif choice == 6:
            v1 = get_vector("Enter first vector (3D, e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (3D, e.g. 4 5 6): ")
            print("Result:", cross_product(v1, v2))
        elif choice == 7:
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            print("Magnitude:", calculate_magnitude(v))
        elif choice == 8:
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Distance:", calculate_distance(v1, v2))
        elif choice == 9:
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            try:
                print("Normalized vector:", normalize_vector(v))
            except ValueError as e:
                print(e)
        elif choice == 10:
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            s = get_scalar("Enter scalar (e.g. 2.5): ")
            print("Amplified vector:", amplify_vector(v, s))
        elif choice == 11:
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            print("Manhattan norm:", calculate_manhattan_norm(v))
        elif choice == 12:
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please select a number from 1 to 12.")

if __name__ == "__main__":
    main()
