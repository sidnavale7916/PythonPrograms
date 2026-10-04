
def is_palindrome_string(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


if __name__ == "__main__":
    print(is_palindrome_string("madam"))
    print(is_palindrome_string("hello"))