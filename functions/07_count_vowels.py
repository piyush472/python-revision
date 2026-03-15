# Question 7: Count vowels
# Write a function count_vowels(s) that counts number of vowels in a string.
def count_vowels(s):
    count=0
    vow="aeiouAEIOU"
    for i in s:
        if i in vow:
            count+=1
    return f"no of vowel in str :{count}"
print(count_vowels("dsfesfesfasfecs"))