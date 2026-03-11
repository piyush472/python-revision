# Question 21: Find odd numbers in list
# Write a Python program to find and print all odd numbers from a list.
l=[1,2,3,4,5,6,7,8,99,8,6,4,3,2,]
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print(l1)