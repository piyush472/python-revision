# PROBLEM :Count vowels
s=input("enter an string:")
count=0
vow="aeiouAEIOU"
for i in s:
    if i in vow:
        count+=1
print(count)