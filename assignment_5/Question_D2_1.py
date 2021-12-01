import C1_us_name_stats as ns

# Case a.
name_list = ns.us_names_top1000.sort()
print(' ' + str(ns.us_names_top1000), '\n', str(name_list))

# Case b.
name_list = ns.us_names_top1000
name_list.sort()
print(' ' + str(ns.us_names_top1000), '\n', str(name_list))

# Case c.
name_list = sorted(ns.us_names_top1000)
print(' ' + str(ns.us_names_top1000), '\n', str(name_list))

