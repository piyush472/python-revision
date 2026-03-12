# Question 9: Merge two dictionaries
# Write a Python program to merge two dictionaries into one.
d1={1:"piyush",2:"rohan",3:"ronit"}
d2={4:"rahul",5:"rohan",6:"ram"}
for key,value in d2.items():
    d1[key]=value
print(d1)