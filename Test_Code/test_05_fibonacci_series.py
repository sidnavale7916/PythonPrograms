
import importlib.util

spec = importlib.util.spec_from_file_location(
    "fibonacci_series",
    "Code/05_fibonacci_series.py"
)

fibonacci_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fibonacci_module)

fibonacci_series = fibonacci_module.fibonacci_series

assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert fibonacci_series(5) == [0, 1, 1, 2, 3]
assert fibonacci_series(1) == [0]
assert fibonacci_series(0) == []
assert fibonacci_series(-3) == []

print("All test cases passed.")