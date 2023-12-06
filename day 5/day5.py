import os
import sys
from typing import List, Tuple

import numpy as np

def read_lines_from_file(file_path: str) -> List[str]:
    """
    Read lines from a file and return a list of strings.

    Parameters:
    - file_path (str): The path to the input file.

    Returns:
    - List[str]: A list of strings representing lines read from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip('\n') for line in file.readlines()]

def get_data(lines: List[str]) -> List[List[List[int]]]:
    """
    Process lines from input and extract data.

    Parameters:
    - lines (List[str]): List of strings representing lines from the input.

    Returns:
    - List[List[List[int]]]: A list of lists of lists of integers representing the data.
    """
    arr_arr = []
    arr = []
    
    for i, line in enumerate(lines[2:]):
        if line == '':
            arr_arr.append(arr)
            arr = []
        else:
            arr.append(line)
    
    arr_arr.append(arr)
    arr_arr = [arr[1:] for arr in arr_arr]
    arr_arr = [[[int(i) for i in item.split(' ')] for item in arr] for arr in arr_arr]
    
    return arr_arr

def mapping(number: int, map_one: List[Tuple[int, int, int]]) -> int:
    """
    Apply mapping to a number using a given mapping.

    Parameters:
    - number (int): The input number.
    - map_one (List[Tuple[int, int, int]]): The mapping to apply.

    Returns:
    - int: The mapped number.
    """
    for trans in map_one:
        if trans[1] <= number < trans[1] + trans[2]:
            index = number - trans[1]
            number_new = trans[0] + index
            return number_new
    
    return number

def mapping_inverse(number: int, map_one: List[Tuple[int, int, int]]) -> int:
    """
    Apply inverse mapping to a number using a given inverse mapping.

    Parameters:
    - number (int): The input number.
    - map_one (List[Tuple[int, int, int]]): The inverse mapping to apply.

    Returns:
    - int: The mapped number.
    """
    for trans in map_one:
        if trans[0] <= number < trans[0] + trans[2]:
            index = number - trans[0]
            number_new = trans[1] + index
            return number_new
    
    return number

def get_complete_mapping_inverse(number: int, maps: List[List[Tuple[int, int, int]]]) -> int:
    """
    Apply complete inverse mapping to a number using a list of inverse mappings.

    Parameters:
    - number (int): The input number.
    - maps (List[List[Tuple[int, int, int]]]): List of inverse mappings.

    Returns:
    - int: The mapped number.
    """
    for map_one in maps:
        number = mapping_inverse(number, map_one)
    
    return number

def get_complete_map(number: int, maps: List[List[Tuple[int, int, int]]]) -> int:
    """
    Apply complete mapping to a number using a list of mappings.

    Parameters:
    - number (int): The input number.
    - maps (List[List[Tuple[int, int, int]]]): List of mappings.

    Returns:
    - int: The mapped number.
    """
    for map_one in maps:
        number = mapping(number, map_one)
    
    return number

def part_1():
    # Specify the path to the input file
    file_path = os.path.join(sys.path[0], 'input.txt')

    lines = read_lines_from_file(file_path)
    seeds = [int(i) for i in lines[0].split(': ')[1].split(' ')]
    maps = get_data(lines)
    
    final = []
    for index, number in enumerate(seeds):
        final.append(get_complete_map(number, maps))
        
        percentage = np.round((index + 1) / len(seeds) * 100, 2)
        print(f'Percentage: {percentage} %', end='\r')
        
    answer = min(final)
    print(f'Answer part 1: {answer}')

def is_in_bounds(bounds_arr: List[List[int]], number: int) -> bool:
    """
    Check if a number is within the given bounds.

    Parameters:
    - bounds_arr (List[List[int]]): List of bounds.
    - number (int): The number to check.

    Returns:
    - bool: True if the number is within bounds, False otherwise.
    """
    for bounds in bounds_arr:
        if bounds[0] <= number < bounds[1]:
            return True
            
    return False

def part_2():
    # Specify the path to the input file
    file_path = os.path.join(sys.path[0], 'input.txt')

    lines = read_lines_from_file(file_path)
    seeds = [int(i) for i in lines[0].split(': ')[1].split(' ')]
    bounds_arr = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]
    maps = get_data(lines)
    maps_inverse = maps[::-1]
    
    number_initial = 0
    while True:
        number_final = get_complete_mapping_inverse(number_initial, maps_inverse)
        print(f'number_final: {number_final} \t\t number_initial: {number_initial}', end='\r')

        if is_in_bounds(bounds_arr, number_final):
            print(f'\n\nAnswer: {number_initial}')
            exit()
        
        number_initial += 1

if __name__ == "__main__":
    part_1()
    part_2()