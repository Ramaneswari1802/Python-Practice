# basic
i=1
while i<5:
 print(i)
 i+=1

#reverse
i=5
while i>0:
 print(i)
 i-=1

# break stmt
i=1
while i<=10:
 if i==5:
  break
 print(i)
 i+=1

#continue stmt
for i in range(1,6):
 if i==3:
  continue
 print(i)

i=1
while i<5:
 if i==3:
  continue
 print(i)
 i+=1

# Task1 (numbers from 1 to 10)
i=1
while i<=10:
 print(i)
 i+=1

#Task2 (print odd from 1 to 15)
i=1
while i<=15:
 if i%2!=0:
  print(i)
 i+=1

# task3(stop if number is 7)
i=1
while i<=10:
 if i==7:
  break
 print(i)
 i+=1

