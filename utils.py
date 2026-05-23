import time
import random

def slow_print(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def roll(chance):
    return random.random() < chance
