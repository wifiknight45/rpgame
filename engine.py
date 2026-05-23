import json
import random
from utils import slow_print

class GameEngine:
    def __init__(self, player, encounters):
        self.player = player
        self.encounters = encounters
        self.story = self.load_story()
        self.current_node = "origin"

    def load_story(self):
        with open("data/story_nodes.json", "r") as f:
            return json.load(f)

    def start_game(self):
        while True:
            node = self.story[self.current_node]
            slow_print(node["text"])

            # Chance-based event
            if random.random() < node.get("event_chance", 0):
                self.encounters.trigger_random_event(self.player)

            # End node
            if node.get("end", False):
                slow_print("Your path concludes.")
                break

            # Present choices
            for choice in node["choices"]:
                print(f"- {choice}")

            user_choice = input("> ").strip().lower()

            if user_choice in node["choices"]:
                self.current_node = node["choices"][user_choice]
            else:
                slow_print("Your indecision shapes nothing. Try again.")
