import itertools
import random

from chess.player import Player


def run():
    players = random.sample((Player("One"), Player("Two")), k=2)

    try:
        for player in itertools.cycle(players):
            input(f"{player.name}'s turn: ")
    
    except KeyboardInterrupt:
        pass
