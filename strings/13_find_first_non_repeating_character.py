# PROBLEM: Find first non repeating character
# Write a program to find the first character that appears only once in the string



s=input("enter an string:")
for i in s:
    a=s.count(i) 
    if a==1:
        print(" first character that appears only once in the string:",i)