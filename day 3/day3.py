import os
import sys
from typing import List, Tuple
import numpy as np

def read_lines_from_file(file_path: str) -> List[str]:
    """Read lines from a file and return a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_surrounding_indices(grid: List[List[str]], row: int, col: int) -> List[Tuple[int, int]]:
    """Get surrounding indices for a given position in a 2D grid."""
    n = len(grid)
    surrounding_indices = [(i, j) for i in range(max(0, row - 1), min(n, row + 2))
                            for j in range(max(0, col - 1), min(n, col + 2))
                            if i != row or j != col]
    return surrounding_indices

def split_string(input_string: str) -> List[str]:
    """Split a string based on non-digit characters and filter out empty strings."""
    result = [item for item in input_string if item.isdigit()]
    return result

def get_numbers_and_indices(lines: List[str], integers: List[str]) -> List[dict]:
    """Extract numbers and their indices from the lines."""
    numbers = []

    for height_index, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i] in integers:
                starting_index = i
                while i < len(line) and line[i] in integers:
                    i += 1

                ending_index = i
                numbers.append({'number': line[starting_index:ending_index],
                                'indices': [(height_index, index) for index in range(starting_index, ending_index)]})
            else:
                i += 1

    return numbers

def remove_duplicates(arr: List[dict]) -> List[dict]:
    """Remove duplicate dictionaries from a list."""
    seen = set()
    result = []

    def tuple_from_dict(d):
        return tuple((k, tuple(v) if isinstance(v, list) else v) for k, v in sorted(d.items()))

    for d in arr:
        tuple_representation = tuple_from_dict(d)

        if tuple_representation not in seen:
            seen.add(tuple_representation)
            result.append(d)

    return result

def part_1():
    """Solution for part 1."""
    file_path = os.path.join(sys.path[0], 'input.txt')
    lines = read_lines_from_file(file_path)

    integers = [str(i) for i in range(10)]
    numbers_and_indices = get_numbers_and_indices(lines, integers)

    numbers_adjacent = []

    for height_index, line in enumerate(lines):
        for width_index, item in enumerate(line):
            if item not in integers and item != '.':
                indices = get_surrounding_indices(lines, row=height_index, col=width_index)

                for index in indices:
                    for item in numbers_and_indices:
                        indices_number = item['indices']
                        if index in indices_number:
                            numbers_adjacent.append(item)

    numbers_final = remove_duplicates(numbers_adjacent)

    final = [item['number'] for item in numbers_final]
    answer = sum(int(item) for item in final)
    print(f'Answer part 1: {answer}')

def part_2():
    """Solution for part 2."""
    file_path = os.path.join(sys.path[0], 'input.txt')
    lines = read_lines_from_file(file_path)

    integers = [str(i) for i in range(10)]
    numbers_and_indices = get_numbers_and_indices(lines, integers)

    gears = []

    for height_index, line in enumerate(lines):
        for width_index, item in enumerate(line):
            if item == '*':
                indices = get_surrounding_indices(lines, row=height_index, col=width_index)

                arr = [item for index in indices for item in numbers_and_indices if index in item['indices']]
                arr = remove_duplicates(arr)

                if len(arr) == 2:
                    gears.append(arr)

    gears = [np.prod([int(item['number']) for item in gear_element]) for gear_element in gears]
    answer = sum(gears)

    print(f'Answer part 2: {answer}')

if __name__ == "__main__":
    part_1()
    part_2()