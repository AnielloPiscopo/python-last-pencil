from typing import NamedTuple
from enum import Enum


class PlayerKind(Enum):
    HUMAN = "human"
    BOT = "bot"

class Player(NamedTuple):
    name: str
    kind: PlayerKind
