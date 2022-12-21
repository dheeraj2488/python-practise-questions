sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d={}
l=[]
for i in sample_list:
    if i not in l:
        l.append(i)
for i in l:
    d[i]=sample_list.count(i)  
print(d)          