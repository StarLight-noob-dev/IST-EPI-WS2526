from random import randint
from typing import List, Tuple


def create_map() -> List[List[str]]:
    r = []
    # for _ in... means we just want to iterate that amount of times and
    # we dont need to keep track of the iterator value
    for _ in range(0,5):
        r.append([".",".",".",".",".",])
    return r

def place_element(game_map: List[List[str]], element: str) -> Tuple[int, int]:
    x = randint(0, 4)
    y = randint(0, 4)
    game_map[x][y] = element
    return x, y

def print_map(game_map: List[List[str]]) -> None:
    # *game_map unpacks the List to get each of the inner list individually
    print(*game_map, sep="\n")

if __name__ == "__main__":
    game = create_map()
    for i in range(2):
        place_element(game, "X")
        place_element(game, "Y")
    print_map(game)