
import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/06_prime_number.py"
)

prime_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prime_module)

is_prime = prime_module.is_prime

assert is_prime(2) is True
assert is_prime(7) is True
assert is_prime(10) is False
assert is_prime(1) is False
assert is_prime(0) is False
assert is_prime(-5) is False

print("All test cases passed.")