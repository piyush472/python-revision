# Question 11: Check prime
# Write a function is_prime(n) that checks whether a number is prime or not.
def is_prime(n):
    prime = True

    if n < 2:
        prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
    return prime
print(is_prime(4))