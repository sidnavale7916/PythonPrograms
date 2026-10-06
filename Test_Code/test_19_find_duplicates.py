
import importlib.util

spec = importlib.util.spec_from_file_location(
    "duplicate_elements",
    "Code/19_find_duplicates.py"
)

duplicate_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(duplicate_module)

find_duplicates = duplicate_module.find_duplicates

assert find_duplicates([1, 2, 3, 2, 4, 3, 5]) == [2, 3]
assert find_duplicates([10, 10, 20, 30, 20]) == [10, 20]
assert find_duplicates([1, 1, 1]) == [1]
assert find_duplicates([1, 2, 3]) == []
assert find_duplicates([]) == []
assert find_duplicates([5, 3, 5, 3, 5]) == [5, 3]

print("All test cases passed.")
