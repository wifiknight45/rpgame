# wizard.py
import random
import time
from utils import slow_print, roll

class WanderingWizard:
    """
    A rich, dynamic wizard companion who follows the player, comments on events,
    offers silly advice, occasionally intervenes with chaotic magic, and very
    rarely does something actually helpful.
    """

    def __init__(self):
        self.name = "Fizzlebottom the Unhelpful"
        self.mood = "mirthful"   # can be 'mirthful', 'miffed', 'philosophical', 'sleepy'
        self.helpfulness = 0.08  # base chance to actually help (8%)
        self.intervention_rate = 0.18  # chance to interject on events
        self.quips = [
            "If you whisper to a question, it might blush.",
            "I once taught a cloud to juggle. It still owes me a coin.",
            "Always carry a spoon. You never know when soup will appear.",
            "If you answer a riddle with a riddle, the riddle gets confused.",
            "I recommend asking the nearest idea for directions.",
            "Never trust a polite echo.",
            "If in doubt, make a hat out of your doubts.",
            "I can neither confirm nor deny the existence of your socks.",
            "A good hat solves 37% of existential problems, approximately.",
            "I once argued with a punctuation mark. It won on a technicality."
        ]
        self.silly_advice = [
            "Try asking the question backwards and see if it answers you.",
            "Sing to the silence. It likes attention.",
            "Offer a compliment to the nearest concept.",
            "Pretend to be a question and see who answers.",
            "If you find a choice you don't like, rename it 'Maybe Later'.",
            "If a choice smells funny, it probably wants a sandwich."
        ]
        self.philosophies = [
            "Meaning is a group project with invisible members.",
            "Sometimes the correct answer is 'more tea'.",
            "Courage is mostly a polite lie you tell your knees."
        ]
        self.taunts = [
            "That was almost clever. Try again with more flair.",
            "You call that a decision? My slippers decide better.",
            "I would help, but I'm currently out of helpfulness."
        ]
        self.rare_helpful_lines = [
            "Ah — a tiny pattern. Try choosing the option that repeats itself.",
            "If you listen to the silence between choices, it hums the right answer.",
            "A small truth: your luck increases when you share snacks with ideas."
        ]
        # small memory of recent interactions to vary responses
        self._recent_comments = []

    # internal helper to print with wizard flavor
    def _speak(self, text, delay=0.01):
        slow_print(f"{self.name} says: {text}", delay)

    # choose a line avoiding immediate repetition
    def _choose_line(self, pool):
        attempts = 0
        while attempts < 6:
            line = random.choice(pool)
            if line not in self._recent_comments:
                break
            attempts += 1
        # maintain a short recent history
        self._recent_comments.append(line)
        if len(self._recent_comments) > 6:
            self._recent_comments.pop(0)
        return line

    # Public: wizard says something random (quips, advice, philosophy, or taunt)
    def say_something(self):
        category_roll = random.random()
        if category_roll < 0.45:
            line = self._choose_line(self.quips)
        elif category_roll < 0.75:
            line = self._choose_line(self.silly_advice)
        elif category_roll < 0.9:
            line = self._choose_line(self.philosophies)
        else:
            line = self._choose_line(self.taunts)
        self._speak(line)

    # Public: react to a story node or event (event is a dict or string)
    def react_to_event(self, event, player=None):
        """
        Called by the engine when a notable event occurs.
        event can be a string description or a dict with keys like 'type' and 'severity'.
        The wizard may comment, intervene, or (rarely) help.
        """
        # small delay for dramatic timing
        time.sleep(0.12)

        # chance to interject at all
        if random.random() > self.intervention_rate:
            # sometimes still mutter a one-liner quietly
            if random.random() < 0.25:
                self._speak(self._choose_line(self.quips))
            return

        # If event is a dict, extract info
        if isinstance(event, dict):
            etype = event.get("type", "mystery")
            severity = event.get("severity", 1)
            desc = event.get("description", "")
        else:
            etype = "mystery"
            severity = 1
            desc = str(event)

        # witty preface
        preface = random.choice([
            "Observe:",
            "Aha!",
            "Hark:",
            "Behold, if you will:"
        ])
        self._speak(f"{preface} {desc}")

        # respond based on type
        if etype == "challenge":
            # more likely to taunt or give silly advice
            if random.random() < 0.6:
                self._speak(self._choose_line(self.silly_advice))
            else:
                self._speak(self._choose_line(self.rare_helpful_lines))
                # tiny chance to actually buff the player
                if player and roll(self.helpfulness * 0.5):
                    self._grant_small_boost(player)
        elif etype == "reward":
            self._speak("Rewards are best enjoyed with a pinch of bewilderment.")
            if player and roll(self.helpfulness * 0.2):
                player.add_item("Wizard's Trinket")
                self._speak("I have bestowed upon you a Wizard's Trinket. Use it wisely-ish.")
        elif etype == "mischief":
            # mischief events get chaotic commentary and sometimes a prank
            self._speak(self._choose_line(self.taunts))
            if roll(0.25):
                self._perform_prank(player)
        else:
            # default reaction
            self._speak(self._choose_line(self.quips))

    # Public: offer advice when the engine presents choices
    def offer_advice(self, choices):
        """
        choices: iterable of choice strings
        Returns: either None (no useful advice) or a suggested choice string.
        The wizard usually gives silly advice; sometimes gives a hint.
        """
        # 40% chance to just be silly
        if random.random() < 0.4:
            self._speak(self._choose_line(self.silly_advice))
            return None

        # 45% chance to give a humorous but harmless suggestion
        if random.random() < 0.85:
            suggestion = random.choice(list(choices))
            hint = random.choice([
                f"Pick '{suggestion}' if you like the sound of it.",
                f"'{suggestion}' has a nice rhythm. Rhythm matters.",
                f"I once knew a choice named '{suggestion}'. It was polite."
            ])
            self._speak(hint)
            return None

        # Rarely, give an actually useful hint (based on internal helpfulness)
        if random.random() < self.helpfulness:
            # try to pick a choice that contains positive words
            for c in choices:
                low = c.lower()
                if any(k in low for k in ("keep", "accept", "follow", "answer", "commit")):
                    self._speak(self._choose_line(self.rare_helpful_lines))
                    return c
            # fallback: return a random choice as a 'hint'
            chosen = random.choice(list(choices))
            self._speak(self._choose_line(self.rare_helpful_lines))
            return chosen

        # default: no useful advice
        self._speak("My advice is a riddle wrapped in a limerick. Interpret at leisure.")
        return None

    # internal: small buff to player (rare)
    def _grant_small_boost(self, player):
        boost = random.choice(["focus", "resolve", "hp"])
        if boost == "focus":
            player.focus += 1
            self._speak("A mote of focus drifts into you. Your thoughts feel tidier.")
        elif boost == "resolve":
            player.resolve += 1
            self._speak("A tiny ember of resolve warms your chest.")
        else:
            player.heal(2)
            self._speak("A whisper of vitality stitches a small patch into you.")

    # internal: perform a harmless prank that may have side effects
    def _perform_prank(self, player):
        pranks = [
            ("tie shoelaces together", "You trip on your own ambition for a moment."),
            ("swap labels", "Your inventory labels rearrange themselves."),
            ("sing a distracting tune", "You lose a beat but gain a new idea.")
        ]
        prank, result_text = random.choice(pranks)
        self._speak(f"I shall now {prank}.")
        time.sleep(0.08)
        self._speak(result_text)
        # small random effect
        if prank == "swap labels" and player.inventory:
            # shuffle inventory names (harmless)
            random.shuffle(player.inventory)
            self._speak("Your items now feel slightly more mysterious.")
        elif prank == "sing a distracting tune":
            # small focus penalty then small resolve gain
            player.focus = max(0, player.focus - 1)
            player.resolve += 1
            self._speak("You lose a sliver of focus but gain a smidge of resolve.")
        else:
            # trip: small hp loss
            player.take_damage(1)
            self._speak("You recover quickly, mostly from embarrassment.")

    # Public: chance to perform a rare, genuinely helpful action
    def attempt_helpful_intervention(self, player):
        """
        Called occasionally by the engine when the player is in trouble.
        Returns True if the wizard performed a helpful action.
        """
        # increase chance slightly if player is low on HP
        hp_factor = 1.0
        if player.hp <= 6:
            hp_factor = 1.6

        chance = self.helpfulness * hp_factor
        if roll(chance):
            # perform a meaningful helpful action
            action = random.choice(["heal", "shield", "reveal"])
            if action == "heal":
                player.heal(4)
                self._speak("By my dubious authority, I mend a few wounds.")
            elif action == "shield":
                player.resolve += 2
                self._speak("I conjure a flimsy shield of polite excuses. It helps.")
            else:
                # reveal a hint about the next choice (engine must use this)
                hint = random.choice(self.rare_helpful_lines)
                self._speak(f"A whisper: {hint}")
            return True
        # otherwise, maybe mutter something unhelpful
        if random.random() < 0.5:
            self._speak(self._choose_line(self.quips))
        return False

    # Public: allow external code to nudge wizard mood (affects lines)
    def set_mood(self, mood):
        if mood in ("mirthful", "miffed", "philosophical", "sleepy"):
            self.mood = mood
        else:
            self.mood = "mirthful"

    # Public: get a short status string for UI or debug
    def status(self):
        return f"{self.name} (mood: {self.mood}, helpfulness: {self.helpfulness:.2f})"
