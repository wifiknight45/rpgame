import random
from utils import slow_print

class WanderingWizard:
    def __init__(self):
        self.name = "Fizzlebottom the Unhelpful"
        self.quips = [
            "If you whisper to a question, it might blush.",
            "I once taught a cloud to juggle. It still owes me a coin.",
            "Always carry a spoon. You never know when soup will appear.",
            "If you answer a riddle with a riddle, the riddle gets confused.",
            "I recommend asking the nearest idea for directions.",
            "Never trust a polite echo.",
            "If in doubt, make a hat out of your doubts.",
            "I can neither confirm nor deny the existence of your socks."
        ]
        self.silly_advice = [
            "Try asking the question backwards and see if it answers you.",
            "Sing to the silence. It likes attention.",
            "Offer a compliment to the nearest concept.",
            "Pretend to be a question and see who answers.",
            "If you find a choice you don't like, rename it 'Maybe Later'."
        ]

    def say_something(self):
        line = random.choice(self.quips + self.silly_advice)
        slow_print(f"{self.name} says: {line}")
