from dataclasses import dataclass
from functools import cached_property

from .pieces import Piece


@dataclass(frozen=True)
class Square:
    rank: int
    file: str

    @cached_property
    def row(self):
        return 8 - self.rank

    @cached_property
    def column(self):
        return ord(self.file) - 65

    @classmethod
    def from_indices(cls, i: int, j: int):
        return cls((8 - i), chr(65 + j))

    def __post_init__(self) -> None:
        if self.rank < 1 or self.rank > 8:
            raise ValueError("Rank out of range")

        if self.file < "A" or self.file > "H":
            raise ValueError("File out of range")
