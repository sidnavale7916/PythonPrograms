
import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_number",
    "Code/09_palindrome_number.py"
)

palindrome_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(palindrome_module)

is_palindrome_number = palindrome_module.is_palindrome_number

assert is_palindrome_number(121) is True
assert is_palindrome_number(123) is False
assert is_palindrome_number(1) is True
assert is_palindrome_number(0) is True
assert is_palindrome_number(1221) is True
assert is_palindrome_number(-121) is False

print("All test cases passed.")