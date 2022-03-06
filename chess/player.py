from dataclasses import dataclass, field

from . import pieces
from .pieces import Piece


@dataclass(frozen=True)
class Player:
    name: str
    pieces: tuple[Piece] = field(default_factory=pieces.starting)
