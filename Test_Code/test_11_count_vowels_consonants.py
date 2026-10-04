
import importlib.util

spec = importlib.util.spec_from_file_location(
    "count_vowels_consonants",
    "Code/11_count_vowels_consonants.py"
)

count_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(count_module)

count_vowels_consonants = count_module.count_vowels_consonants

assert count_vowels_consonants("Hello World") == (3, 7)
assert count_vowels_consonants("Python") == (1, 5)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("BCDFG") == (0, 5)
assert count_vowels_consonants("123 !") == (0, 0)
assert count_vowels_consonants("") == (0, 0)

print("All test cases passed.")