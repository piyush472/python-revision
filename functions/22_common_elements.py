# Question 22: Common elements
# Write a function common_elements(lst1, lst2) that returns common elements between two lists.
def common_elements(lst1, lst2):
    result=[]
    for i in lst1:
        if i in lst2 and i not in result:
            result.append(i)
    return result

print(common_elements([1,2,3,4,5], [3,4,5,6,7]))
