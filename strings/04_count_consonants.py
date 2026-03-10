# PROBLEM :Count consonants
s=input("enter an string:")
count=0
vow="aeiouAEIOU"
for i in s:
    if i not in vow:
        count+=1
print(count)