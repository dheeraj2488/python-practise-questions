# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
a=speed.values()
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(l)        
