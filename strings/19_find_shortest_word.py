# PROBLEM: Find shortest word
# Write a program to find the shortest word in a sentence
s = input("Enter a sentence: ")
print(min(s.split(), key=len))