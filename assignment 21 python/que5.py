first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
c=tuple(first_list)
d=tuple(second_list)
a=set(zip(c,d))
print(a)

