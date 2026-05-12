# Question 31: Group by first letter
# Write a Python program to group a list of words into a dict by their first letter.
words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry', 'apricot', 'cat']
d = {}
for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]].append(word)
print(d)
