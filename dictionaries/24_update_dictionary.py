# Question 24: Update dictionary
# Write a Python program to update a dictionary with another dictionary or key-value pairs.
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