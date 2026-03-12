# PROBLEM: Find longest word
# Write a program to find the longest word in a sentence
s = input("Enter a sentence: ")
print(max(s.split(), key=len))