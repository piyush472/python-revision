# PROBLEM: Reverse words in sentence
# Write a program to reverse the order of words in a sentence
s=input("enter an string:")
l=[]
for i in s.split():
    l.append(i[-1::-1])
new_s=" ".join(l)
print(new_s)