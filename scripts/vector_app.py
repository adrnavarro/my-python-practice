"""
vector_app.py
=============

A command-line application for performing a variety of vector operations interactively.

This script provides a menu-driven interface to perform addition, subtraction, multiplication, division, dot product, cross product, magnitude, distance, normalization, amplification, and Manhattan norm calculations on vectors. It utilizes functions from modules.vetor_operations and numpy for computation.

Typical Usage:
--------------
1. Activate your virtual environment.
2. Run the script from the project root or src directory:

    python3 -m scripts.vector_app

3. Follow the on-screen menu to select and perform vector operations.
4. To exit, select the 'Exit' option or press Ctrl+C.

Notes:
------
- Input vectors as space-separated numbers (e.g., 1 2 3).
- Handles invalid input gracefully and prompts for re-entry.
- Designed for educational and demonstration purposes.
"""

import sys
import numpy as np
from modules.vetor_operations import (
    add_vectors, subtract_vectors, multiply_vectors, divide_vectors,
    dot_product, cross_product, calculate_magnitude, calculate_distance,
    normalize_vector, amplify_vector, calculate_manhattan_norm
)

# --- User Input Helpers ---

def get_vector(prompt: str) -> np.ndarray:
    """
    Prompt the user to input a vector and return it as a numpy array of floats.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        np.ndarray: The vector entered by the user as a numpy array of floats.

    Raises:
        Recursively prompts until valid input is provided.
    """
    raw = input(prompt)

    # Attempt to parse the input as a vector of floats
    try:
        vec = np.array([float(x) for x in raw.strip().split()])
        return vec
    except Exception:
        print("Invalid input. Please enter numbers separated by spaces.")
        return get_vector(prompt)

def get_scalar(prompt: str) -> float:
    """
    Prompt the user to input a scalar value and return it as a float.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        float: The scalar value entered by the user.

    Raises:
        Recursively prompts until valid input is provided.
    """
    raw = input(prompt)

    # Attempt to parse the input as a float
    try:
        return float(raw.strip())
    except Exception:
        print("Invalid input. Please enter a number.")
        return get_scalar(prompt)

# --- Main Application Loop ---

def main() -> None:
    """
    Main function to run the interactive vector operations menu.

    Presents a menu of vector operations, handles user input, and calls the appropriate
    vector operation functions. Loops until the user chooses to exit.
    """

    # Define the menu options for vector operations
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

        # Display the menu options
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")
        try:
            # Get the user's menu choice
            choice = int(input("Select an option (1-12): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Handle each menu option
        if choice == 1:

            # Add two vectors
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", add_vectors(v1, v2))
        elif choice == 2:

            # Subtract two vectors
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", subtract_vectors(v1, v2))
        elif choice == 3:

            # Multiply two vectors element-wise
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", multiply_vectors(v1, v2))
        elif choice == 4:

            # Divide two vectors element-wise
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", divide_vectors(v1, v2))
        elif choice == 5:

            # Dot product of two vectors
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Result:", dot_product(v1, v2))
        elif choice == 6:

            # Cross product of two 3D vectors
            v1 = get_vector("Enter first vector (3D, e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (3D, e.g. 4 5 6): ")
            print("Result:", cross_product(v1, v2))
        elif choice == 7:

            # Calculate magnitude of a vector
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            print("Magnitude:", calculate_magnitude(v))
        elif choice == 8:

            # Calculate distance between two vectors
            v1 = get_vector("Enter first vector (e.g. 1 2 3): ")
            v2 = get_vector("Enter second vector (e.g. 4 5 6): ")
            print("Distance:", calculate_distance(v1, v2))
        elif choice == 9:

            # Normalize a vector
            v = get_vector("Enter vector (e.g. 1 2 3): ")

            # Try to normalize the vector and handle errors
            try:
                print("Normalized vector:", normalize_vector(v))
            except ValueError as e:
                print(e)
        elif choice == 10:

            # Amplify a vector by a scalar
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            s = get_scalar("Enter scalar (e.g. 2.5): ")
            print("Amplified vector:", amplify_vector(v, s))
        elif choice == 11:

            # Calculate Manhattan norm (L1) of a vector
            v = get_vector("Enter vector (e.g. 1 2 3): ")
            print("Manhattan norm:", calculate_manhattan_norm(v))
        elif choice == 12:

            # Exit the application
            print("Exiting. Goodbye!")
            sys.exit(0)
        else:

            # Handle invalid menu option
            print("Invalid option. Please select a number from 1 to 12.")

if __name__ == "__main__":
    main()
