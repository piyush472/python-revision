# problem :Print multiplication table
a=1
num=int(input("enter an no whose table u want:"))
for i in range(1,11):
    print(num,"X",a,"=",num*a)
    a+=1