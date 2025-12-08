from itertools import cycle
from typing import Iterator,Optional
from utils.num_utils import get_num_in_range , get_num
from utils.iterator_utils import get_el_in_iterable , get_str_by_iterable , get_list_str
from classes import *
from custom_exceptions import ConstraintError,ConversionError


def get_players_names() -> tuple[Player, ...]:
    return (
        Player("John", PlayerKind.HUMAN),
        Player("Jack", PlayerKind.BOT),
    )


def get_pencils_num()->Optional[int]:
    print("How many pencils would you like to use:")

    while True:
        try:
            return get_num_in_range(0)
        except ConstraintError:
            print("The number of pencils should be positive")
        except ConversionError:
            print("The number of pencils should be numeric")

def play_game(players:tuple[Player,...], pencils_num:int)->None:
    current_player: Player = get_first_player(players)
    turn_order:Iterator[Player] = cycle(players)

    for p in turn_order:
        if p == current_player:
            break

    while pencils_num > 0:
        print_lines(pencils_num)
        pencils_num -= play_turn(current_player , pencils_num)
        current_player = next(turn_order)

    if pencils_num == 0:
        print(current_player.name + "won!")

def get_first_player(players:tuple[Player,...])->Player:
    players_names:tuple[str,...] = tuple(p.name for p in players)

    print(get_str_by_iterable(players_names,
                           ", ","(", "):",
                           "Who will be the first "))

    while True:
        try:
            chosen_name:str = get_el_in_iterable(players_names)

            return next(p for p in players if p.name == chosen_name)
        except ConstraintError:
            print(get_str_by_iterable(players_names,
                                   "' and '", "'", "'",
                                   "Choose between "))

def print_lines(pencils_num:int)->None:
    print("|" * pencils_num)
    

def play_turn(player:Player, pencils_num)->int:
    print(player.name + "'s turn:")

    if player.kind == PlayerKind.BOT:
        move:int = get_bot_move(pencils_num)
        print(move)
        return move

    pencils_gotten: int = 0

    while True:
        max_pencils_to_get:int = 3

        try:
            pencils_gotten = get_num_in_range(0, max_pencils_to_get)
        except (ConversionError ,ConstraintError):
            print(get_str_by_iterable(range(1 , max_pencils_to_get+1),
                                      "', '" , "'" , "'" ,
                                      "Possible values: "," or '"))
            continue

        try:
            if pencils_gotten > pencils_num:
                raise ConstraintError
            else:
                break
        except ConstraintError:
            print("Too many pencils were taken")


    return pencils_gotten

def get_bot_move(pencils_num: int) -> int:
    # posizione perdente: 1, 5, 9, 13... → n % 4 == 1
    if pencils_num % 4 == 1:
        return 1

    r = pencils_num % 4
    return 3 if r == 0 else r - 1
