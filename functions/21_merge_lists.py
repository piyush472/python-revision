# Question 21: Merge two lists
# Write a function merge_lists(lst1, lst2) that merges two lists.
def merge_lists(lst1, lst2):
    merged=[]
    for i in lst1:
        merged.append(i)
    for i in lst2:
        merged.append(i)
    return merged

print(merge_lists([1,2,3], [4,5,6]))
