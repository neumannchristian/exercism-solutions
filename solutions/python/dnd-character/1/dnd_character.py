import random
import math


class Character:
    def __init__(self):
        self.strength = roll_dice()
        self.dexterity = roll_dice()
        self.constitution = roll_dice()
        self.intelligence = roll_dice()
        self.wisdom = roll_dice()
        self.charisma = roll_dice()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        ability_values = list(self.__dict__.values())[:6]
        return ability_values[random.randrange(6)]


def roll_dice():
    throws = [random.randrange(1, 6) for _ in range(4)]
    throws.sort()
    return sum(throws[:3])


def modifier(value):
    return math.floor((value - 10) / 2)
