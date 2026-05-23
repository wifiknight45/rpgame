#!/usr/bin/env python3

from engine import GameEngine
from player import Player
from utils import slow_print
from encounters import initialize_encounters

def main():
    slow_print("=== WELCOME TO THE TRIAL OF CHOICES ===")
    name = input("Identify yourself: ")

    player = Player(name)
    encounters = initialize_encounters()
    engine = GameEngine(player, encounters)

    engine.start_game()

if __name__ == "__main__":
    main()
