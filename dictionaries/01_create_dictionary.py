# Question 1: Create dictionary
# Write a Python program to create a dictionary and print it.
no_ele=int(input("enter no of elememt u want in dict :"))
d={}
for i in range(1,no_ele+1):
    key=int(input("enter an key "))
    value=input("enter value :")
    d[key]=value
print(d)
