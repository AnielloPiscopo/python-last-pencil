from game import get_players_names,get_pencils_num,play_game
from classes import Player


def main()->None:
    players:tuple[Player,...] = get_players_names()
    pencils_num:int = get_pencils_num()
    play_game(players, pencils_num)

if __name__ == '__main__':
    main()