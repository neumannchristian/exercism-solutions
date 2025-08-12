def sum_of_multiples(limit, multiples):
    filtered = set()
    for item_base in multiples:
        if item_base == 0:
            continue
        multiple = item_base
        index = 1
        while multiple < limit:
            filtered.add(multiple)
            index += 1
            multiple = index * item_base

    return sum(filtered)
