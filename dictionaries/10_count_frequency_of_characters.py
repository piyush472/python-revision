# Question 10: Count frequency of characters
# Write a Python program to count the frequency of each character in a string using a dictionary.
s="adadaddnjanljjajljdsnljndljan"
d={}

for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
