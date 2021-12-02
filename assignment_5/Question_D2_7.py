import C1_us_name_stats as ns

"""
    This function returns the index of a name if it is found otherwise return -1
    The function has two parameters: the search name, and a list of sorted name
    There is a inner function also:
        --> the binary search function is a recursive function
        --> has two parameters: the lower and upper bound
        --> two base conditions: 1. if lower index is larger than upper then the element is not found
        -->                      2. if the element is found
"""


def build_index(_list: []) -> dict:
    # here, index is a dictionary which hold the name as key and value as original index
    _index = {_list[_ind]: _ind for _ind in range(len(_list))}
    return _index


def find_name_fast(_name: str, _sortedlist: []) -> int:
    # this is the inner function
    def binary_search(_lower: int, _upper: int) -> int:
        # if we search all the list and couldn't found the data then have to stop the execution.
        if _lower > _upper:
            return -1

        # calculate the middle of the array
        _mid = int((_lower + _upper) / 2)

        if _sortedlist[_mid] > _name:
            return binary_search(_lower, _mid - 1)
        elif _sortedlist[_mid] < _name:
            return binary_search(_mid + 1, _upper)
        else:
            return _mid

    return binary_search(0, len(_sortedlist))


name_list = ns.us_names_top1000
sorted_list = sorted(name_list)
name_freq = ns.us_name_freq_top1000

# call the build_index method return a dictionary which has name as key and index of it as value
index = build_index(name_list)

names = ['Smith', 'Mendoza', 'Rodriguez', 'Abbott', 'Blokes', 'Brewer', 'Vang', 'Zimmerman', 'Bailey']

for n in names:
    i = find_name_fast(n, sorted_list)
    print(str(i) + '\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[index.get(n)]) if i >= 0 else "")
