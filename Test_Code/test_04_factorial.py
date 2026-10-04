
import importlib.util

spec = importlib.util.spec_from_file_location(
    "factorial",
    "Code/04_factorial.py"
)

factorial_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(factorial_module)

factorial = factorial_module.factorial

assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(3) == 6
assert factorial(1) == 1
assert factorial(-2) == "Invalid input"

print("All test cases passed.")