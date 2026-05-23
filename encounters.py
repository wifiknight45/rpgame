import random
from utils import slow_print

class EncounterSystem:
    def __init__(self, events):
        self.events = events

    def trigger_random_event(self, player):
        event = random.choice(self.events)
        slow_print(event["description"])

        outcome_roll = random.random()

        if outcome_roll < event["harm_chance"]:
            damage = random.randint(1, event["max_harm"])
            player.take_damage(damage)
        else:
            reward = event["reward"]
            player.inventory.append(reward)
            slow_print(f"You gain: {reward}")

def initialize_encounters():
    return EncounterSystem([
        {
            "description": "A surge of doubt tests your inner strength.",
            "harm_chance": 0.5,
            "max_harm": 4,
            "reward": "Clarity Fragment"
        },
        {
            "description": "A whisper of insight brushes your mind.",
            "harm_chance": 0.2,
            "max_harm": 2,
            "reward": "Insight Spark"
        },
        {
            "description": "A shadow of uncertainty looms.",
            "harm_chance": 0.7,
            "max_harm": 5,
            "reward": "Resolve Ember"
        }
    ])
