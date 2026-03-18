# Question 17: Sum of digits
# Write a function sum_digits(n) that returns sum of digits of a number.
def sum_digits(n):
    total=0
    for digit in str(n):
        total+=int(digit)
    return total
print(sum_digits(12345))

    