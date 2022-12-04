# Write a Python function to multiply all the numbers in a list

# Sample List : (8, 2, 3, -1, 7)

# Expected Output : -336
def multiply(list):
    mul=1
    for i in list:
        mul=mul*i
    return mul
list=[8,2,3,-1,7]
print(multiply(list))        
