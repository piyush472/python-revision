# Question 23: Anagram check
# Write a function is_anagram(s1, s2) that checks whether two strings are anagrams.
def is_anagram(s1, s2):
    s1_sorted=sorted(s1.lower())
    s2_sorted=sorted(s2.lower())
    if s1_sorted==s2_sorted:
        return True
    else:
        return False

print(is_anagram("listen", "silent"))
