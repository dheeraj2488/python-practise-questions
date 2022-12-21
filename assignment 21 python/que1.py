l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
nl=[]
nl2=[]
for i in range(0,len(l1)):
    if i%2!=0:
        a=l1[i]
        nl.append(a)
for i in range(0,len(l2)):   
    if i%2==0:
        b=l2[i]
        nl2.append(b)
print(nl+nl2)        


        
      

   