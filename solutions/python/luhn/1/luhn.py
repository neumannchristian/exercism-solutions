class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        scrubbed = list(self.card_num.replace(" ", ""))
        if len(scrubbed) <= 1:
            return False
        scrubbed.reverse()
        result = []
        for idx, char in enumerate(scrubbed):
            if not char.isdigit():
                return False
            char = int(char)
            if not idx % 2 == 0:
                char *= 2
            if char > 9:
                char -= 9
            result.append(char)
        return sum(result) % 10 == 0
