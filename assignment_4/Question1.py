def is_sorted(_list: []) -> bool:
    if len(_list) == 0 or len(_list) == 1:
        return True

    if len(_list) == 2:
        if _list[0] <= _list[1]:
            return True
        return False
    else:
        if _list[0] > _list[1]:
            return False
        return is_sorted(_list[1:])


numbers = [
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 9],
    [4, 8, 12, 12, 24, 36],
    [], [2], [1, 2], [2, 1]]

for n in numbers:
    print(str(is_sorted(n)) + '\t<-- ' + str(n))
