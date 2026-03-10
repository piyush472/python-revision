# PROBLEM: Count frequency of character
# Write a program to count how many times a specific character appears in a string

count=0
chara="a"
s=input("enter an string:")
for i in s:
    if i==chara:
        count+=1
print(count)