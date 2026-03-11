# Question 19: Check if list is palindrome
# Write a Python program to check if a list is a palindrome (reads the same forward and backward).
l=[1,2,3,2,1]
if l[-1::-1]==l:
    print("list is palindrome!")
else:
        print("list is not palindrome!")