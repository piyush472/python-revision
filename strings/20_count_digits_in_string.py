# PROBLEM: Count digits in string
# Write a program to count how many digits are present in a string
import string
s=input("enter an string:")
count=0
dig=string.digits
for i in s:
    if i in dig:
        count+=1
print(count)
