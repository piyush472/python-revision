# PROBLEM: Find first non repeating character
# Write a program to find the first character that appears only once in the string



s = input("enter a string:")

for i in s:
    if s.count(i) == 1:
        print("first non repeating character:", i)
        break