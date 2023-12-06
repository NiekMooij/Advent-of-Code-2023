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

def get_upper_lower_bound(time: float, distance: float) -> Tuple[float, float]:
    """
    Calculate upper and lower bounds based on time and distance.

    Parameters:
    - time (float): The time value.
    - distance (float): The distance value.

    Returns:
    - Tuple[float, float]: Lower and upper bounds.
    """
    upper_bound = 1/2 * (time + np.sqrt(time**2 - 4*distance))
    lower_bound = 1/2 * (time - np.sqrt(time**2 - 4*distance))
    
    return lower_bound, upper_bound

def get_numbers_in_bound(lower_bound: float, upper_bound: float) -> List[int]:
    """
    Get numbers within a specified range.

    Parameters:
    - lower_bound (float): The lower bound.
    - upper_bound (float): The upper bound.

    Returns:
    - List[int]: List of numbers within the specified range.
    """
    return [i for i in range(int(lower_bound-1), int(upper_bound+1)) if i > lower_bound and i < upper_bound]

def part_1():
    file_path = os.path.join(sys.path[0], 'input.txt')

    lines = read_lines_from_file(file_path) 
    
    times = [int(i) for i in lines[0].split(':')[1:][0].split(' ') if i]
    distances = [int(i) for i in lines[1].split(':')[1:][0].split(' ') if i]

    arr = []
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
    
        lower_bound, upper_bound = get_upper_lower_bound(time, distance)
        answer = get_numbers_in_bound(lower_bound, upper_bound)
        
        arr.append(len(answer))        
    
    print(f'Answer part 1: {np.prod(arr)}')
    
def part_2():
    time = 48989083
    distance = 390110311121360

    lower_bound, upper_bound = get_upper_lower_bound(time, distance)
    answer = get_numbers_in_bound(lower_bound, upper_bound)
    
    print(f'Answer part 2: {len(answer)}')

if __name__ == "__main__":
    part_1()
    part_2()