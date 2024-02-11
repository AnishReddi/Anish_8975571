from string_utils import reverse_string, capitalize_string, is_palindrome

def test_integration():
    assert is_palindrome(reverse_string("radar")) == True
    assert is_palindrome(capitalize_string("hello")) == False
    assert reverse_string("hello") == "olleh"

def test_integration_2():
    assert reverse_string("olleh") == "helo"

# def test_reverse_string():
#     assert reverse_string("hello") == "olleh"
#     assert reverse_string("12345") == "54321"
#     assert reverse_string("") == ""
#
#
# def test_capitalize_string():
#     assert capitalize_string("hello") == "Hello"
#     assert capitalize_string("12345") == "12345"
#     assert capitalize_string("") == ""
#
#
# def test_is_palindrome():
#     assert is_palindrome("radar") == True
#     assert is_palindrome("level") == True
#    ## assert is_palindrome("Able was I ere I saw Elba") == True
#     assert is_palindrome("hello") == False







# if __name__ == '__main__':
#     test_reverse_string()
#     test_capitalize_string()
#     test_is_palindrome()
#     test_integration()
#     print("All tests passed!")
