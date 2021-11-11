def log_printer(_a, _b, _log):
    print(f'{_a} < {_b} -> {_log}')


def is_sorted(_list: [], _log: bool = False) -> bool:

    if len(_list) == 0 or len(_list) == 1:
        return True

    if len(_list) == 2:
        if _list[0] <= _list[1]:
            log_printer(_list[0], _list[1], True)
            return True
        return False
    else:
        if _list[0] > _list[1]:
            log_printer(_list[0], _list[1], False)
            return False
        log_printer(_list[0], _list[1], True)
        return is_sorted(_list[1:])


numbers = [
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 9],
    [4, 8, 12, 12, 24, 36],
    [], [2], [1, 2], [2, 1]]

n = numbers[0]  # [1, 2, 3, 0, 4, 5, 6, 7, 8, 9]

print("==>")
print(str(is_sorted(n, True)) + '\t<-- ' + str(n))
