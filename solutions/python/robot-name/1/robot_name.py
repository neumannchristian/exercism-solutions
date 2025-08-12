import random


class Robot:
    def __init__(self):
        self._history = []
        self.name = self.generate_name()

    def generate_name(self):
        result = ""
        for _ in range(2):
            result += chr(random.randrange(65, 91))
        for _ in range(3):
            result += str(random.randrange(9))
        self._history.append(result)
        return result

    def reset(self):
        new_name = self.generate_name()
        if new_name in self._history:
            self.name = self.generate_name()
