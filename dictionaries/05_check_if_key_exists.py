# Question 5: Check if key exists
# Write a Python program to check if a given key exists in a dictionary.
from threading import get_ident


d = {
    "name": "Piyush",
    "age": 21,
    "is_student": True,
    "city": "Delhi"
}
given_key="name"
if given_key in d.keys():
    print("given key exists in dictionary!")
else:
     print("given key not exists in dictionary!")
