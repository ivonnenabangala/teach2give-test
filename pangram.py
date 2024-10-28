# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example:
# "The quick brown fox jumps over the lazy dog"
import re, string

def pangram(text):
    text = text.lower()
    alphabet_match = re.findall(r'[a-z]', text)
    alphabet_set = set(alphabet_match)

    return set(string.ascii_lowercase) == alphabet_set

def test():
    print(pangram("The quick brown fox jumps over the lazy dog"))
    print(pangram("Hey"))

test()
