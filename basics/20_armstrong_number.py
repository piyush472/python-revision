# problem:  Armstrong number check
num = int(input("Enter a number: "))
original = num
n = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** n
    num //= 10

if sum == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")   
    