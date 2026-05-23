#!/usr/bin/env python3

from engine import GameEngine
from player import Player
from wizard import WanderingWizard
from utils import slow_print

def main():
    slow_print("=== TRIALS OF THE ABSURD REALM ===")
    name = input("Name your essence: ").strip() or "Nameless One"

    player = Player(name)
    wizard = WanderingWizard()
    engine = GameEngine(player, wizard)

    engine.start_game()

if __name__ == "__main__":
    main()

