# Question 16: Fibonacci sequence
# Write a function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c

fibonacci(10)
