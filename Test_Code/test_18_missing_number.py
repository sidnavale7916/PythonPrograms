
import importlib.util

spec = importlib.util.spec_from_file_location(
    "missing_number",
    "Code/18_missing_number.py"
)

missing_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(missing_module)

find_missing_number = missing_module.find_missing_number

assert find_missing_number([1, 2, 4, 5], 5) == 3
assert find_missing_number([1, 3, 4, 5], 5) == 2
assert find_missing_number([1, 2, 3, 5], 5) == 4
assert find_missing_number([2, 3, 4, 5], 5) == 1
assert find_missing_number([1, 2, 3, 4], 5) == 5
assert find_missing_number([], 1) == 1

print("All test cases passed.")