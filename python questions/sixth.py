def unique(list):
    x=[]
    for i in list:
        if i not in x:
            x.append(i)
    return x
list=[1, 2, 5, 2, 5, 1, 3, 7, 9]
print(unique(list))            