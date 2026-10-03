
import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest_of_three",
    "Code/02_largest_of_three.py"
)

largest_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(largest_module)

largest_of_three = largest_module.largest_of_three

assert largest_of_three(10, 25, 15) == 25
assert largest_of_three(50, 20, 30) == 50
assert largest_of_three(5, 5, 2) == 5
assert largest_of_three(-1, -5, -3) == -1
assert largest_of_three(7, 7, 7) == 7

print("All test cases passed.")