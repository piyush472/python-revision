# Question 18: Rotate list
# Write a Python program to rotate a list left or right by a given number of positions.
#right rotation
l = [1,2,3,4,5]
k = 2

new_l = l[k:] + l[:k]

print(new_l)
#right rotation
l = [1,2,3,4,5]
k = 2

new_l = l[-k:] + l[:-k]

print(new_l)