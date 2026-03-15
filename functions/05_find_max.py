# Question 5: Find maximum of two numbers
# Write a function find_max(a, b) that returns the larger number.
def find_max(a, b):
    if a>b:
        return f"{a} is greater then {b}"
    else:
        return f"{b} is greater then {a}"
print(find_max(2,4))
