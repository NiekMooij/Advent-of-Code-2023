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
        return [line.strip() for line in file.readlines()]

def get_price(intersection: List[str]) -> int:
    """
    Calculate the price based on the length of the intersection of winning and owned cards.

    Parameters:
        intersection (List[str]): List of common elements between winning and owned cards.

    Returns:
        int: Calculated price.
    """
    length = len(intersection)
    
    if length == 1:
        return 1
    
    else:
        return int(2**(length-1))

def part_1(lines: List[str]) -> None:
    """
    Calculate and print the answer for Part 1.

    Parameters:
        lines (List[str]): List of input lines containing winning and owned cards information.
    """
    count = 0

    for line in lines:
        winning_cards, owned_cards = line.split(' | ')
        winning_cards = winning_cards.split(': ')[1]
        winning_cards = [item for item in winning_cards.split(' ') if item]
        owned_cards = [item for item in owned_cards.split(' ') if item]
        intersection = list(set(winning_cards) & set(owned_cards))
        count += get_price(intersection)
        
    print(f'Answer part 1: {count}')

def get_intersection(card: Dict[str, any]) -> List[str]:
    """
    Get the intersection of winning and owned numbers for a given card.

    Parameters:
        card (Dict[str, any]): Dictionary containing information about a card.

    Returns:
        List[str]: List of common elements between winning and owned numbers.
    """
    winning_numbers = card['winning_numbers']
    owned_numbers = card['owned_numbers']
    intersection = [i for i in winning_numbers if i in owned_numbers]
    return intersection

def part_2(lines: List[str]) -> None:
    """
    Calculate and print the answer for Part 2.

    Parameters:
        lines (List[str]): List of input lines containing winning and owned cards information.
    """
    cards = {}

    # Make cards object
    for line in lines:
        winning_numbers, owned_numbers = line.split(' | ')
        id, winning_numbers = winning_numbers.split(': ')
        id = id.split(' ')[-1]
        winning_numbers = [item for item in winning_numbers.split(' ') if item]
        owned_numbers = [item for item in owned_numbers.split(' ') if item]
        cards[id] = {'amount': 1, 'winning_numbers': winning_numbers, 'owned_numbers': owned_numbers}
        
    for id, card in cards.items():
        intersection = get_intersection(card)
        cards_new_ids = [str(i) for i in list(range(int(id)+1, int(id)+1+len(intersection)))]

        for id_new in cards_new_ids:
            if id_new in cards.keys():
                cards[id_new]['amount'] = cards[id_new]['amount'] + cards[id]['amount']
    
    answer = sum([card['amount'] for _, card in cards.items()])
    
    print(f'Answer part 2: {answer}')

if __name__ == "__main__":
    # Specify the path to the input file
    file_path = os.path.join(sys.path[0], 'input.txt')

    lines = read_lines_from_file(file_path)

    part_1(lines)
    part_2(lines)