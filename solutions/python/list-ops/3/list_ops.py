def append(list1, list2):
    return list1 + list2


def concat(lists):
    flat = []
    for el in lists:
        if isinstance(el, list):
            flat.extend(el)
        else:
            flat.append(el)
    return flat


def filter(function, list):
    return [el for el in list if function(el)]


def length(list):
    return sum([1 for el in list])


def map(function, list):
    return [function(el) for el in list]


def foldl(function, list, initial):
    result = initial
    for el in list:
        result = function(result, el)
    return result


def foldr(function, list, initial):
    result = initial
    for el in list[::-1]:
        result = function(result, el)
    return result


def reverse(list):
    return [list[index] for index in range(len(list)-1,-1,-1)]
