list1 = [54, 44, 27, 79, 91, 41]
a=list1[4]
list1.remove(a)
print(list1)
list1.insert(2,a)
print(list1)
list1.insert(list1[-1],a)
print(list1)