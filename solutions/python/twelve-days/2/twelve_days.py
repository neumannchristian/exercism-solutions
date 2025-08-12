def recite(start_verse, end_verse):
    ELEMENTS = {
        1: ("first", "a Partridge in a Pear Tree"),
        2: ("second", "two Turtle Doves"),
        3: ("third", "three French Hens"),
        4: ("fourth", "four Calling Birds"),
        5: ("fifth", "five Gold Rings"),
        6: ("sixth", "six Geese-a-Laying"),
        7: ("seventh", "seven Swans-a-Swimming"),
        8: ("eighth", "eight Maids-a-Milking"),
        9: ("ninth", "nine Ladies Dancing"),
        10: ("tenth", "ten Lords-a-Leaping"),
        11: ("eleventh", "eleven Pipers Piping"),
        12: ("twelfth", "twelve Drummers Drumming"),
    }

    def build_verse(number):
        header = (
            f"On the {ELEMENTS[number][0]} day of Christmas my true love gave to me: "
        )

        if number == 1:
            return f"{header}{ELEMENTS[1][1]}."
        return f"{header}{', '.join([ELEMENTS[i][1] for i in range(number, 1, -1)])}, and {ELEMENTS[1][1]}."

    return [build_verse(i) for i in range(start_verse, end_verse + 1)]


print(recite(1, 1))
