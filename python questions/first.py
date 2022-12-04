# Write a Python function to find the Max of three numbers
def largest(a,b,c):
    if a>b and a>c:
        largest=a
    elif b>a and b>c:
        largest=b
    elif c>a and c>b:
        largest=c
    return largest            
a=input()
b=input()
c=input()
print(largest(a,b,c))
