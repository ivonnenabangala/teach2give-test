# 2. Write a Python function that checks whether a word or phrase is palindrome or
# not.
# Note: A palindrome is word, phrase, or sequence that reads the same
# backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def palindrome(text):
    text = text.replace(' ','')
    reversed_text = text[::-1]
    return text == reversed_text

def test_function():
  testCases = ["madam", "nurses run", "hello", "racecar", "kayak", "word"]
  for test in testCases:
      if palindrome(test):
          print(f"{test} is palindrome")
          # return True
      else:
          print(f"{test} is not palindrome")
          # return False
test_function()