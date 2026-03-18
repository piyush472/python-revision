# Question 20: Count character occurrences
# Write a function count_char(s, ch) that counts how many times a character appears in a string.
def count_char(s, ch):
    count=0
    for i in s:
        if i==ch:
            count+=1
    return count

print(count_char("hello world", "l"))
