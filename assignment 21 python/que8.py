# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:
roll_number = [47, 64, 69, 37, 76, 83, 97]
sampleDict = {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

for i in roll_number:
    if not i in sampleDict.values():
        roll_number.remove(i)
print(roll_number)        