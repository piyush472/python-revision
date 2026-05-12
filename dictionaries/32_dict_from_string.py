# Question 32: Dict from string
# Write a Python program to count frequency of each word in a sentence using a dict.
s = 'the cat sat on the mat the cat'
d = {}
for word in s.split():
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)
