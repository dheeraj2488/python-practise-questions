sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
l=[]
for i in sample_list:
    if i not in l:
        l.append(i)
b=tuple(l)
print(b)
print(max(b),min(b))
        