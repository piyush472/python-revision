# Question 25: Count upper and lower case
# Write a function count_upper_lower(s) that returns number of uppercase and lowercase letters.
def count_upper_lower(s):
    upper=0
    lower=0
    for i in s:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    return upper, lower

print(count_upper_lower("HeLLo WoRLd"))
