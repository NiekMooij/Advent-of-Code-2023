import os
import sys
from typing import List, Dict

def read_lines_from_file(file_path: str) -> List[str]:
    """Read lines from a file and return a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_info(lines: List[str]) -> Dict[int, List[Dict[str, int]]]:
    """
    Parse the input lines to extract information about games and their attributes.

    Args:
    - lines (List[str]): List of strings containing information about games.

    Returns:
    - Dict[int, List[Dict[str, int]]]: A dictionary where the key is the game ID and the value
      is a list of dictionaries representing each game's attributes.
    """
    info = {}
    for line in lines:
        # Split the line into ID part and information part
        id_part, info_part = line.split(': ')
        game_id = int(id_part.split(' ')[1])

        # Split the information part into individual games
        games = info_part.split('; ')

        games_arr = []
        for game in games:
            game_info = {}
            # Extract values and colors for each attribute in a game
            for item in game.split(', '):
                value, color = item.split(' ')
                game_info[color] = int(value)

            games_arr.append(game_info)

        info[game_id] = games_arr

    return info

def is_game_possible(game: List[Dict[str, int]], red_max: int, green_max: int, blue_max: int) -> bool:
    """
    Check if a given game is possible based on the maximum allowed values for each color.

    Args:
    - game (List[Dict[str, int]]): List of dictionaries representing the attributes of the game.
    - red_max (int): Maximum allowed value for the 'red' color.
    - green_max (int): Maximum allowed value for the 'green' color.
    - blue_max (int): Maximum allowed value for the 'blue' color.

    Returns:
    - bool: True if the game is possible within the specified limits, False otherwise.
    """
    for item in game:
        if 'red' in item and item['red'] > red_max:
            return False

        if 'green' in item and item['green'] > green_max:
            return False

        if 'blue' in item and item['blue'] > blue_max:
            return False

    return True

def get_minimum_set_of_cubes(game: List[Dict[str, int]]) -> List[int]:
    """
    Get the minimum set of cubes required for a game.

    Args:
    - game (List[Dict[str, int]]): List of dictionaries representing the attributes of the game.

    Returns:
    - List[int]: List of the maximum values for each color in the game.
    """
    red_values = []
    green_values = []
    blue_values = []
    for item in game:
        if 'red' in item:
            red_values.append(item['red'])
        if 'green' in item:
            green_values.append(item['green'])
        if 'blue' in item:
            blue_values.append(item['blue'])
        
    minimum_set_of_cubes = [max(red_values), max(green_values), max(blue_values)]
    
    return minimum_set_of_cubes
    
def get_power_of_minimum_set(minimum_set_of_cubes: List[int]) -> int:
    """
    Calculate the power of the minimum set of cubes.

    Args:
    - minimum_set_of_cubes (List[int]): List of the maximum values for each color.

    Returns:
    - int: The product of the values in the minimum_set_of_cubes.
    """
    return minimum_set_of_cubes[0] * minimum_set_of_cubes[1] * minimum_set_of_cubes[2]

def part_1():
    # Construct file path relative to the script location
    file_path = os.path.join(sys.path[0], 'input.txt')

    # Read lines from the file
    lines = read_lines_from_file(file_path)
    info = get_info(lines)
    
    red_max, green_max, blue_max = 12, 13, 14
    
    count = 0
    arr = []
    for game_id, game in info.items():
        if is_game_possible(game, red_max, green_max, blue_max):
            count += game_id
            arr.append(game_id)
                
    print(f'Answer part 1: {sum(list(set(arr)))}')
    
def part_2():
    # Construct file path relative to the script location
    file_path = os.path.join(sys.path[0], 'input.txt')

    # Read lines from the file
    lines = read_lines_from_file(file_path)
    info = get_info(lines)
    
    count = 0
    for game_id, game in info.items():
        minimum_set_of_cubes = get_minimum_set_of_cubes(game)
        power_of_minimum_set = get_power_of_minimum_set(minimum_set_of_cubes)
        
        count += power_of_minimum_set
        
    print(f'Answer part 2: {count}')

if __name__ == "__main__":
    part_1()
    part_2()