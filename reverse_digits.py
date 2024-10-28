# 4. Write a program that takes an integer as input and returns an integer
# with reversed digit ordering.

def reverse_digits(n):
    reversed_digits = str(n)[::-1]
    if n < 0:
        reversed_digits = str(n)[:0:-1]
        return int('-' + reversed_digits)
    return int(reversed_digits)

def test_function():
  testCases = [91, 1, 500, -56, -90]
  for digit in testCases:
      print(reverse_digits(digit))

test_function()