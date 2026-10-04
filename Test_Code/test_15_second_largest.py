
import importlib.util

spec = importlib.util.spec_from_file_location(
    "second_largest",
    "Code/15_second_largest.py"
)

largest_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(largest_module)

second_largest = largest_module.second_largest

assert second_largest([10, 20, 4, 45, 99]) == 45
assert second_largest([5, 5, 3, 2]) == 3
assert second_largest([1, 2]) == 1
assert second_largest([7, 7, 7]) is None
assert second_largest([]) is None
assert second_largest([-1, -5, -3]) == -3

print("All test cases passed.")