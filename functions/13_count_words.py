# Question 13: Count words
# Write a function count_words(sentence) that returns number of words in a sentence.
def count_words(sentence):
    count=0
    for i in sentence.split():
        count+=1
    return count
print(count_words("sa adad ada dad efde"))