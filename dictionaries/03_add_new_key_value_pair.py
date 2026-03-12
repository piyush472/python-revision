# Question 3: Add new key value pair
# Write a Python program to add a new key-value pair to an existing dictionary.
d = {
    "name": "Piyush",
    "age": 21,
    "is_student": True,
    "city": "Delhi"
}
n=int(input("enter no of key ,value u wnat to add:"))
for i in range(1,n+1):
    key=input("enter an key:")
    value=input("enter an value:")
    d[key]=value
print(d)