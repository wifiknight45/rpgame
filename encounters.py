import random
from utils import slow_print

class EncounterSystem:
    def __init__(self):
        # abstract events and playful outcomes
        self.events = [
            {
                "description": "A sudden Pop of Curiosity tests your focus.",
                "harm_chance": 0.3,
                "max_harm": 3,
                "reward": "Curiosity Shard"
            },
            {
                "description": "A Mischief Breeze rearranges your thoughts.",
                "harm_chance": 0.5,
                "max_harm": 4,
                "reward": "Mischief Trinket"
            },
            {
                "description": "A Helpful Nonsense appears and offers a riddle.",
                "harm_chance": 0.2,
                "max_harm": 2,
                "reward": "Riddle Token"
            },
            {
                "description": "A Tiny Paradox winks and hands you a questionable map.",
                "harm_chance": 0.4,
                "max_harm": 3,
                "reward": "Questionable Map"
            }
        ]

    def trigger_random_event(self, player, wizard=None):
        event = random.choice(self.events)
        slow_print(event["description"])

        # Wizard commentary rarely helpful
        if wizard and random.random() < 0.4:
            wizard.say_something()

        outcome_roll = random.random()
        # luck slightly reduces harm
        luck_factor = max(0.1, 1.0 - (player.luck - 1.0) * 0.1)
        effective_harm_chance = event["harm_chance"] * luck_factor

        if outcome_roll < effective_harm_chance:
            damage = random.randint(1, event["max_harm"])
            player.take_damage(damage)
            slow_print("The event leaves a bruise on your confidence.")
            if not player.is_alive():
                slow_print("Your essence fades into a footnote of the absurd.")
                exit()
        else:
            reward = event["reward"]
            player.add_item(reward)
            slow_print(f"You receive {reward} and a faint sense of bemusement.")
