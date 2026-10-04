
import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

palindrome_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(palindrome_module)

is_palindrome_string = palindrome_module.is_palindrome_string

assert is_palindrome_string("madam") is True
assert is_palindrome_string("hello") is False
assert is_palindrome_string("Racecar") is True
assert is_palindrome_string("nurses run") is True
assert is_palindrome_string("") is True
assert is_palindrome_string("Python") is False

print("All test cases passed.")