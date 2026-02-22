# taking input
name=input("enter name:")
print(name)

# with integer
age=int(input("enter age:"))
print(age)

# multiple inputs in one line

print("enter a and b values")
a,b=map(int,input().split())
print(a+b)

# comparison

print(a>b)
print(a==b)
print(a<b)
print(a!=b)
print(a>b and a<20)
print(a>56 or b<90)
print(not(a>5))


# Task
''' take two numbers, print sum, check first greater than second, 
check both are positive using logical operator
'''

x,y=map(int,input().split())
print(x+y)
print(x>y)
print(x>0 and y>0)