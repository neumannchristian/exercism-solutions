import random


class Robot:
    def _generate_name(self):
        letters = [chr(random.randrange(65, 91)) for _ in range(2)]
        numbers = [str(random.randrange(9)) for _ in range(3)]
        return "".join(letters + numbers)

    def reset(self):
        while (name := self._generate_name()) in self._history:
            pass
        self._history.add(name)
        self.name = name

    def __init__(self):
        self._history = set()
        self.reset()
