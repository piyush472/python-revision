# Question 26: Rotate list
# Write a function rotate_list(lst, k) that rotates list by k positions.
# Example: rotate_list([1,2,3,4,5], 2) → [4,5,1,2,3] (right rotate)
def rotate_list(lst, k):
    k=k%len(lst)
    rotated=lst[-k:]+lst[:-k]
    return rotated

print(rotate_list([1,2,3,4,5], 2))
