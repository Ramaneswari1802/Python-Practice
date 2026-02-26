arr = [8, 3, 12, 5]
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)