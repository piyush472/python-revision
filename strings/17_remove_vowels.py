# PROBLEM: Remove vowels
# Write a program that removes all vowels from a given string

s=input("enter an string:")
vow="AEIOUaeiou"
l=[]

for i in s:
    if i not in vow:
        l.append(i)
new_s="".join(l)
print(new_s)