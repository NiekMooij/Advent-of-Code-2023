import os
import sys
from typing import List, Tuple
import networkx as nx

def read_lines_from_file(file_path: str) -> List[str]:
    """
    Read lines from a file and return a list of strings.
    
    Parameters:
    - file_path (str): The path to the input file.
    
    Returns:
    - List[str]: A list of strings representing lines read from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_surrounding_indices(grid: List[List[str]], row: int, col: int) -> List[Tuple[int, int]]:
    """
    Get surrounding indices for a given position in a 2D grid.
    
    Parameters:
    - grid (List[List[str]]): The 2D grid.
    - row (int): The row index.
    - col (int): The column index.
    
    Returns:
    - List[Tuple[int, int]]: A list of tuples representing surrounding indices.
    """
    n = len(grid)
    surrounding_indices = []

    for i in range(max(0, row - 1), min(n, row + 2)):
        for j in range(max(0, col - 1), min(n, col + 2)):
            if i != row or j != col:
                surrounding_indices.append((i, j))

    return surrounding_indices

if __name__ == "__main__":
    # Specify the path to the input file
    file_path = os.path.join(sys.path[0], 'input.txt')
    # file_path = os.path.join(sys.path[0], 'test.txt')

    # Read the grid from the file
    grid = read_lines_from_file(file_path)

    # Get the dimensions of the grid
    width = len(grid[0])
    height = len(grid)

    # Define a list of valid integers and the '.' character
    integers = [str(i) for i in range(10)]
    integers.extend('.')
    arr = []
    
    
    for line in grid:
        for item in line:
            if item not in integers: