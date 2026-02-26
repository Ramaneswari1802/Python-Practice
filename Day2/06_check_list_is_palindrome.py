arr = [1, 2, 3, 2, 1]
left=arr[0]
right=arr[-1]
for i in range(len(arr)):
    if left!=right:
        print("Not a palindrome")
        break
    else:
        left=arr[i]
        right=arr[-(i+1)]
print("Palindrome")

# method2

arr = [1, 2, 3, 2, 1]

left = 0
right = len(arr) - 1
is_palindrome = True

while left < right:
    if arr[left] != arr[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)