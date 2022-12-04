# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
def add(list):
    add=0
    for i in list:
        add=add+i
    return add
list=[63,5,3,2,6,4]
print(add(list))

