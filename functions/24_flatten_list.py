# Question 24: Flatten nested list
# Write a function flatten_list(lst) that converts a nested list into a single list.
# Example: [[1,2],[3,4],[5]] → [1,2,3,4,5]
def flatten_list(lst):
    result=[]
    for i in lst:
        for j in i:
            result.append(j)
    return result

print(flatten_list([[1,2],[3,4],[5]]))
