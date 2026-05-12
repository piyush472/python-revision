# Question 32: Dict from string
# Write a Python program to count frequency of each word in a sentence using a dict.
s = "the cat sat on the mat the cat"
d={}
for i in s.split():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)