# Question 25: Flatten nested list
# Write a Python program to flatten a nested list (list of lists) into a single list.
l = [["apple","banana"], ["mango"], ["grape","orange"]]
l1=[]
for i in l:
    for j in i:
        l1.append(j)
print(l1)