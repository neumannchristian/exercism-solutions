def find(search_list, value):
    low = 0
    high = len(search_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if value > search_list[mid]:
            low = mid + 1
        elif value < search_list[mid]:
            high = mid - 1
        else:
            return mid
    raise ValueError("value not in array")
