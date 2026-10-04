
import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_string",
    "Code/12_reverse_string.py"
)

reverse_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reverse_module)

reverse_string = reverse_module.reverse_string

assert reverse_string("Python") == "nohtyP"
assert reverse_string("Hello") == "olleH"
assert reverse_string("a") == "a"
assert reverse_string("") == ""
assert reverse_string("12345") == "54321"
assert reverse_string("Hello World") == "dlroW olleH"

print("All test cases passed.")