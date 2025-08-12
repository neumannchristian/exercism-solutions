import re


class PhoneNumber:
    def parse_number(self, string):
        scrubbed = (
            string.replace(" ", "")
            .replace("-", "")
            .replace("(", "")
            .replace(")", "")
            .replace(".", "")
            .replace("+", "")
        )

        if len(scrubbed) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(scrubbed) > 11:
            raise ValueError("must not be greater than 11 digits")

        if len(scrubbed) == 11:
            if scrubbed[0] != "1":
                raise ValueError("11 digits must start with 1")
            scrubbed = scrubbed[1:]

        area_code = scrubbed[:3]
        exchange_code = scrubbed[3:6]

        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if re.search(r"[a-zA-Z]+", area_code):
            raise ValueError("letters not permitted")
        if re.search(r"\W+", area_code):
            raise ValueError("punctuations not permitted")

        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")
        if re.search(r"[a-zA-Z]+", exchange_code):
            raise ValueError("letters not permitted")
        if re.search(r"\W+", exchange_code):
            raise ValueError("punctuations not permitted")

        subscriber_number = scrubbed[6:]

        self.area_code = area_code
        self.exchange_code = exchange_code
        self.subscriber_number = subscriber_number

        return scrubbed

    def __init__(self, number):
        self.number = self.parse_number(number)

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
