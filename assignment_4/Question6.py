import C1_us_name_stats as ns


def find_name(_name: str, _list: []) -> int:
    _indices = list(filter(lambda _ind: _list[_ind] == _name, range(len(_list))))
    return _indices[0] if len(_indices) == 1 else -1


name_list = ns.us_names_top1000
name_freq = ns.us_name_freq_top1000

names = ['Smith', 'Mendoza', 'Rodriguez', 'Abbott', 'Blokes', 'Brewer',
         'Vang', 'Zimmerman', 'Bailey']
for n in names:
    i = find_name(n, name_list)
    print(str(i) + '\t\t<-- ' + str(n), end='')
    print('\t\t--> freq: ' + str(name_freq[i]) if i >= 0 else "")