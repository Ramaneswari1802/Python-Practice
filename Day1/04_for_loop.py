# basic
for i in range(5):
    print(i)

#range(start,end)
for i in range(10,20):
    print(i)

#range(start,end,step)
for i in range(10,20,3):
    print(i)

# loop in list
arr=[10,20,40]
for i in arr:
    print(i)

#loop through string
name="rama"
for i in name:
    print(i)

# using index in loop
arr=[10,63,45,87]
for i in range(len(arr)):
    print(i,arr[i])

# Task1

# print from 1 to 10
for i in range(1,11):
    print(i)

#Task2(print only even numbers from 1 to 20)
for i in range(1,21):
    if i%2==0:
        print(i)

# task3(sum of numbers from 1 to 5)
a=0
for i in range(6):
    a+=i
    i+=1
print(a)

#task4(count nu of vowels in a string)
count=0
ex="AEIOUaeiou"
str="Rama"
for i in str:
    if i in ex:
        count+=1
print(count)

