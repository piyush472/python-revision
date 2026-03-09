# problem:  Factorial of a number
num=int(input("enter no whose factorial u want:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)