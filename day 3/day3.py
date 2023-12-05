import os
import sys
from typing import List, Tuple

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

def has_element_not_in_other_array(array1: List[str], array2: List[str]) -> bool:
    """
    Check if any element in array1 is not present in array2.
    
    Parameters:
    - array1 (List[str]): First list of elements.
    - array2 (List[str]): Second list of elements.
    
    Returns:
    - bool: True if any element in array1 is not in array2, False otherwise.
    """
    for element in array1:
        if element not in array2:
            return True
    return False

def split_string(input_string: str) -> List[str]:
    """
    Split a string based on non-digit characters and filter out empty strings.
    
    Parameters:
    - input_string (str): The input string.
    
    Returns:
    - List[str]: A list of substrings containing only digits.
    """
    for char in input_string:
        if char not in [str(i) for i in range(10)]:
            input_string = input_string.replace(char, '.')

    result = [item for item in input_string.split('.') if item]
    return result

def process_line_numbers(line: str, integers: List[str], grid: List[List[str]]) -> List[str]:
    """
    Process numbers in a given line and return a list of numbers that have invalid surroundings.
    
    Parameters:
    - line (str): The line containing numbers to be processed.
    - integers (List[str]): List of valid integers and the '.' character.
    - grid (List[List[str]]): The 2D grid.
    
    Returns:
    - List[str]: A list of numbers with specific element in it's surrounding.
    """
    numbers = split_string(line)
    indices = [line.find(number) for number in numbers]
    numbers_and_indices = [(numbers[i], list(range(indices[i], indices[i] + len(numbers[i])))) for i in range(len(numbers))]

    invalid_numbers = []

    for number, indices in numbers_and_indices:
        surrounding_indices = []

        for index in indices:
            surrounding_indices.extend(get_surrounding_indices(grid, grid.index(line), index))

        surrounding_elements = list(set([grid[i][j] for i, j in list(set(surrounding_indices))]))

        if has_element_not_in_other_array(surrounding_elements, integers):
            invalid_numbers.append(number)

    return invalid_numbers

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
    
    # Process each line and gather invalid numbers
    for line in grid:
        part_numbers = process_line_numbers(line, integers, grid)
        arr.extend(part_numbers)
    
    for e in arr:
        print(e)
        
    # Print the sum of the integers found in the grid
    print(f'Answer: {sum([int(item) for item in arr])}')
    
    print(grid[0])
    
    # 528799
