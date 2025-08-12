def recite(start_verse, end_verse):
    ELEMENTS = {
        1: ("first", "a Partridge in a Pear Tree."),
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
        verse_parts = [
            f"On the {ELEMENTS[number][0]} day of Christmas my true love gave to me:"
        ]

        gifts = []
        for i in range(number, 0, -1):
            gift_phrase = ELEMENTS[i][1]
            if i == 1 and number > 1:
                gifts.append(f"and {gift_phrase}")
            else:
                gifts.append(gift_phrase)

        gifts_string = ""
        if len(gifts) == 1:
            gifts_string = gifts[0]
        else:
            gifts_string = ", ".join(gifts[:-1])
            if number > 1:
                gifts_string = f"{gifts_string}, {gifts[-1]}"
            else:
                gifts_string = gifts[0]

        return f"{verse_parts[0]} {gifts_string}"

    verses_output = []
    for i in range(start_verse, end_verse + 1):
        verses_output.append(build_verse(i))

    return verses_output
