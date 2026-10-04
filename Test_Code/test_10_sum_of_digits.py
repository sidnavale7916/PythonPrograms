
import importlib.util

spec = importlib.util.spec_from_file_location(
    "sum_of_digits",
    "Code/10_sum_of_digits.py"
)

sum_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sum_module)

sum_of_digits = sum_module.sum_of_digits

assert sum_of_digits(1234) == 10
assert sum_of_digits(567) == 18
assert sum_of_digits(0) == 0
assert sum_of_digits(9) == 9
assert sum_of_digits(-123) == 6
assert sum_of_digits(1000) == 1

print("All test cases passed.")