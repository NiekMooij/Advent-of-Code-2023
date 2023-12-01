import os
import sys
from typing import List, Tuple, Union

def read_lines_from_file(file_path: str) -> List[str]:
    """Read lines from a file and return a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_integers_and_index(line: str) -> List[Tuple[int, Union[str, int]]]:
    """
    Extract integers and their indices from a given string.

    Args:
        line (str): Input string.

    Returns:
        List[Tuple[int, Union[str, int]]]: List of tuples containing index and integer representation.
    """
    result = []

    # Extract numeric digits
    for index, element in enumerate(line):
        if element.isdigit():
            result.append((index, int(element)))

    # Extract words representing numbers
    for integer_word, integer_str in string_to_int_mapping.items():
        index = line.find(integer_word)

        while index != -1:
            result.append((index, int(integer_str)))
            index = line.find(integer_word, index + 1)

    return result

def calculate_total(lines: List[str]) -> int:
    """
    Calculate the total sum of integers extracted from a list of strings.

    Args:
        lines (List[str]): List of input strings.

    Returns:
        int: Total sum of integers.
    """
    total_sum = 0

    for line in lines:
        indices_and_integers = get_integers_and_index(line)
        sorted_indices_and_integers = sorted(indices_and_integers, key=lambda x: x[0])

        # Retrieve the first and last integers from the sorted list
        first_integer = sorted_indices_and_integers[0][1]
        last_integer = sorted_indices_and_integers[-1][1]

        # Convert word representations to actual integers using the mapping
        if isinstance(first_integer, str):
            first_integer = string_to_int_mapping[first_integer]

        if isinstance(last_integer, str):
            last_integer = string_to_int_mapping[last_integer]

        # Calculate the value and add to the total sum
        value = int(str(first_integer) + str(last_integer))
        total_sum += value

    return total_sum

if __name__ == "__main__":
    # Define mapping of word representations to integer values
    string_to_int_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Construct file path relative to the script location
    file_path = os.path.join(sys.path[0], 'input.txt')

    # Read lines from the file
    lines = read_lines_from_file(file_path)

    # Calculate the total sum of integers and print the result
    total_sum = calculate_total(lines)
    print("Total Sum of Integers:", total_sum)
