# Question 19: Second largest in list
# Write a function find_second_largest(lst) that returns second largest number in list.
def find_second_largest(lst):
    sorted_list=sorted(lst)
    return sorted_list[-2]

print(find_second_largest([1,2,3,4,5]))
