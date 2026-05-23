import json
import random
from utils import slow_print, ask_choice
from encounters import EncounterSystem

class GameEngine:
    def __init__(self, player, wizard):
        self.player = player
        self.wizard = wizard
        self.story = self.load_story()
        self.current_node = "origin"
        self.encounters = EncounterSystem()

    def load_story(self):
        with open("data/story_nodes.json", "r") as f:
            return json.load(f)

    def start_game(self):
        slow_print(f"Guide: {self.wizard.name} will accompany you and say odd things.")
        while True:
            node = self.story[self.current_node]
            slow_print("\n" + node["text"])

            # Wizard interjection sometimes
            if random.random() < node.get("wizard_chance", 0.25):
                self.wizard.say_something()

            # Chance-based event
            if random.random() < node.get("event_chance", 0.2):
                self.encounters.trigger_random_event(self.player, self.wizard)

            # If node ends the path
            if node.get("end", False):
                slow_print(node.get("ending_text", "The sequence resolves."))
                break

            # Present choices as questions and silly answers
            choice = ask_choice(node["choices"])
            next_node = node["choices"].get(choice)

            if next_node:
                self.current_node = next_node
            else:
                slow_print("Your hesitation becomes a riddle. The world waits.")

