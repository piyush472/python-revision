# PROBLEM: Remove special characters
# Write a program to remove all special characters from a string (keep only letters and numbers)
import string as ss
l=[]
s=input("enter an string:")
spe=ss.punctuation
for i in s:
    if i not in spe:
        l.append(i)
new_s="".join(l)
print(new_s)