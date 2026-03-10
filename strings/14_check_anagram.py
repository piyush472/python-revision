# PROBLEM: Check anagram
# Write a program that checks if two strings are anagrams of each other

s=input("enter an string:")
s2=input("enter an string:")
a=sorted(s.lower())
b=sorted(s2.lower())
if a==b:
    print("given string is anagram!")
else:
     print("given string is not anagram!")