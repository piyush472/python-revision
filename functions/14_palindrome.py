# Question 14: Palindrome check
# Write a function palindrome(s) that checks whether a string is palindrome.
def palindrome(s):
    if s==s[-1::-1]:
        return True
    else:
        return False
print("string is palindrome:",palindrome("adafefefefefefeaaaaaaa"))