# PROBLEM: Find longest word
# Write a program to find the longest word in a sentence
s="my name is piyush"

a=s.split()
l=[] 
for i in a:
    l.append(len(i))
print(max(l))