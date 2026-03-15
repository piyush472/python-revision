# Question 10: Find length without len()
# Write a function find_length(s) that returns the length of a string without using len().
def find_length(s):
    count_a=0
    for i in s:
        count_a+=1
    return count_a
print((f"lth of str:"),find_length("dsfesfesfasfecs"))