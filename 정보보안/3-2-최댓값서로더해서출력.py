def do_list_max_gob(l1, l2): return int(max(l1)) * int(max(l2))


print(do_list_max_gob(input().rstrip().split(','), input().rstrip().split(',')))
