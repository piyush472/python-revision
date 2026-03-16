# Question 15: Remove duplicates from list
# Write a function remove_duplicates(lst) that removes duplicates from a list.
def remove_duplicates(lst):
    l2=[]
    for i in lst:
        if i not in l2:
            l2.append(i)
    return l2
print(remove_duplicates([1,2,1,23,5,3,2,3,55,3,21,2,3,4]))
