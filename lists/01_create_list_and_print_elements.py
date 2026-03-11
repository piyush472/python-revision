# Question 1: Create list and print elements
# Write a Python program to create a list and print all its elements.
l=[]
no_ele=int(input("enter no of element u want in list :"))
for i in range(1,no_ele+1):
    ele=int(input("enter element:"))
    l.append(ele)
print(l)