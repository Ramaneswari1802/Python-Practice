# basic if
a=19
if a>18:
    print("eligible")

#if else

num=7
if num%2==0:
    print("even")
else:
    print("odd")

#if elif else(used when multiple conditons exit)

marks=85
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
else:
    print("c")

# nested if

n=30
if n>0:
    if n%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("negative")

# Task
''' take input, check, is positive,is negative,is zero, 
if positive check even or odd'''

number=int(input("Enter number:"))
if number==0:
    print("zero")
elif number>0:
    if number%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    print("negative")

