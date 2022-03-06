from functools import total_ordering
from math import inf


@total_ordering
class Piece:
    __slots__ = ("VALUE",)

    def __lt__(self, other) -> bool:
        """Needed for `total_ordering` and more generally for comparing
        value of pieces"""

        return self.VALUE < other.VALUE
    
    def __eq__(self, other) -> bool:
        """Needed for `total_ordering` and more generally for comparing
        value of pieces"""

        return self.VALUE == other.VALUE

    def __radd__(self, other):
        """Facilitates summing, used for totalling points"""

        if isinstance(other, int):
            return self.VALUE + other

        return self.VALUE + other.VALUE


class Pawn(Piece):
    VALUE = 1

    def __str__(self) -> str:
        return (" (_)\n"
                " / \\\n"
                "-----")


class Knight(Piece):
    VALUE = 3

    def __str__(self) -> str:
        return ("/_o^\\\n"
                " /  /\n"
                "-----")


class Bishop(Piece):
    VALUE = 3

    def __str__(self) -> str:
        return (" //\\\n"
                "(/  )\n"
                "-----")


class Rook(Piece):
    VALUE = 5

    def __str__(self) -> str:
        return ("|_|_|\n"
                "/   \\\n"
                "-----")


class Queen(Piece):
    VALUE = 9

    def __str__(self) -> str:
        return ("\\\\|//\n"
                " \\ /\n"
                "-----")


class King(Piece):
    VALUE = inf

    def __str__(self) -> str:
        return ("  +\n"
                "( | )\n"
                "-----")


def starting() -> tuple[Piece]:
    return (Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(),
            Rook(), Knight(), Bishop(), King(), Queen(), Bishop(), Knight, Rook())
