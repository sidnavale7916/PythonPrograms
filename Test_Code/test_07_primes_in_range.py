
import importlib.util

spec = importlib.util.spec_from_file_location(
    "primes_in_range",
    "Code/07_primes_in_range.py"
)

primes_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(primes_module)

primes_in_range = primes_module.primes_in_range

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(10, 20) == [11, 13, 17, 19]
assert primes_in_range(1, 5) == [2, 3, 5]
assert primes_in_range(2, 2) == [2]
assert primes_in_range(-5, 1) == []
assert primes_in_range(10, 5) == []

print("All test cases passed.")