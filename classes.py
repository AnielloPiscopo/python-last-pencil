from typing import NamedTuple
from enum import Enum


class PlayerKind(Enum):
    """
    Enum that represents the type of player.
    """
    HUMAN = "human"
    BOT = "bot"

class Player(NamedTuple):
    """
    Immutable structure representing a player.
    """
    name: str
    kind: PlayerKind
