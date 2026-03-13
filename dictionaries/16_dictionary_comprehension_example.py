# Question 16: Dictionary comprehension example
# Write a Python program demonstrating dictionary comprehension (e.g., create {n: n**2} for n in range).
d={}
n=3
for i in range(1,n+1):
    d[i]=i**2

print(d)