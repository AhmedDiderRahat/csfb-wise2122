def generate(_items: [int]) -> [[int]]:
    res = [[]]
    for item in _items:
        new_set = [r + [item] for r in res]
        res.extend(new_set)
    return res


print(f'The sequences are = {generate([0, 1, 2])}')
