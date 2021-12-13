list4 = [['c', 2], ['d', 1], ['a', 3], ['b', 5], ['c', 1], ['c', 3]]

print(sorted(list4, key=lambda x : (x[0], x[1])))
print(list4)