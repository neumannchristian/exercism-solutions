def recite(start_verse, end_verse):
    phrases = [
        ("house that Jack built", ""),
        ("malt", "lay in"),
        ("rat", "ate"),
        ("cat", "killed"),
        ("dog", "worried"),
        ("cow with the crumpled horn", "tossed"),
        ("maiden all forlorn", "milked"),
        ("man all tattered and torn", "kissed"),
        ("priest all shaven and shorn", "married"),
        ("rooster that crowed in the morn", "woke"),
        ("farmer sowing his corn", "kept"),
        ("horse and the hound and the horn", "belonged to"),
    ]

    verses = []

    def build_verse(number):
        line = f"This is the {phrases[number-1][0]}" 
        for index in range(number-1,0, -1):
            # print(elements[index][1])
            action = phrases[index][1]
            line += f" that {action} the {phrases[index-1][0]}"
        return line + "."

    for verse_number in range(start_verse, end_verse+1):
        verses.append(build_verse(verse_number))

    return verses
