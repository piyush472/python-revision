# Question 18: Capitalize words
# Write a function capitalize_words(sentence) that capitalizes the first letter of each word.
def capitalize_words(sentence):
    words=sentence.split()
    result=""
    for word in words:
        result+=word.capitalize()+" "
    return result.strip()

print(capitalize_words("hello world from python"))
