import os
import sys
from typing import List, Tuple, Dict

def read_lines_from_file(file_path: str) -> List[str]:
    """
    Read lines from a file and return a list of strings.
    
    Parameters:
    - file_path (str): The path to the input file.
    
    Returns:
    - List[str]: A list of strings representing lines read from the file.
    """
    with open(file_path, 'r') as file:
        return [ line.strip('\n') for line in file.readlines()]

if __name__ == "__main__":
    # Specify the path to the input file
    file_path = os.path.join(sys.path[0], 'test.txt')

    lines = read_lines_from_file(file_path)
    
    for line in lines:
        print(line)
        
    print(lines[3])
