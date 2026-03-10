# PROBLEM: Count words in sentence
# Write a program that takes a sentence as input and prints the number of words in it

s=input("enter sentence:")
count=0
for i in s.split():
    count+=1
print(count)