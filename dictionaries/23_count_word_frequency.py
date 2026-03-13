# Question 23: Count word frequency
# Write a Python program to count the frequency of each word in a sentence using a dictionary.
s="adjkasldaljhsjhgdkgbahbkhnjlslhndjfas"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)