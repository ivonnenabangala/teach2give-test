def pascal_case(text):
    text = text.title()
    return text

def test():
    test_cases = input("Enter a test case: ")
    # for test in test_cases:
    print(pascal_case(test_cases))
test()