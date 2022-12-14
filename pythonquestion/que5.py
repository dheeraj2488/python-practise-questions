# Check if the first and last number of a list is the same.
# Expected Output - 
# A = [10, 11, 50, 58, 29, 10]
# Output - True

# B = [10000, 11, 50, 58, 29, 10]
# Output - False
a=list(map(int,input().split(",")))
if a[0]==a[-1]:
    print("True")
else:
    print("False")    