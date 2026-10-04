
def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


if __name__ == "__main__":
    print(reverse_string("Python"))
    print(reverse_string("Hello"))