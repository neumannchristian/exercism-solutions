YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    counts = [dice.count(i) for i in range(1, 7)]

    print(counts)
    unique_dice = sorted(list(set(dice)))

    match category:
        case 0:
            if 5 in counts:
                return 50
        case 1:
            return counts[0] * 1
        case 2:
            return counts[1] * 2
        case 3:
            return counts[2] * 3
        case 4:
            return counts[3] * 4
        case 5:
            return counts[4] * 5
        case 6:
            return counts[5] * 6
        case 7:
            if sorted(counts) == [0,0,0,0,2,3]:
                return sum(dice)
        case 8:
            for i, count in enumerate(counts):
                if count >= 4:
                    return (i + 1) * 4
        case 9:
            if unique_dice == [1,2,3,4,5]:
                return 30
        case 10:
            if unique_dice == [2,3,4,5,6]:
                return 30
        case 11:
            return sum(dice)
    return 0
