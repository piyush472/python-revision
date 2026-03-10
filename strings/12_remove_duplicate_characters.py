# PROBLEM: Remove duplicate characters
# Write a program that removes duplicate characters from a string (keep first occurrence)
l=[]
st=""
s=input("enter an string:")
for i in s:
    if i not in l:
        l.append(i)
new_str="".join(l)
print(new_str)