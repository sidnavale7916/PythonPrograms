
import importlib.util

spec = importlib.util.spec_from_file_location(
    "pos_neg_zero",
    "Code/03_pos_neg_zero.py"
)

pos_neg_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pos_neg_module)

pos_neg_zero = pos_neg_module.pos_neg_zero

assert pos_neg_zero(10) == "Positive"
assert pos_neg_zero(-5) == "Negative"
assert pos_neg_zero(0) == "Zero"
assert pos_neg_zero(100) == "Positive"
assert pos_neg_zero(-100) == "Negative"

print("All test cases passed.")