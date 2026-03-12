# PROBLEM: Check if string contains substring
# Write a program that checks if one string contains another string as substring
s=input("enter an string:")
ano_str=input("enter an substring:")
if ano_str in s:
    print(ano_str ,"is a substring of",s)
else:
     print(ano_str ,"is not a substring of",s)