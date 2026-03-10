# problem :  Count digits in a number
num=int(input("enter an number:"))
count=0
s=str(num)
for i in s:
    count+=1
print("no of digit in ",num,":",count)