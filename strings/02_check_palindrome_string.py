# PROBLEM :Check palindrome string
s=input("enter an string:")
if s==s[-1::-1]:
    print("given string is palindrome")
else:
    print("given string is not palindrome")