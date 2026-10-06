
import importlib.util

spec = importlib.util.spec_from_file_location(
    "character_frequency",
    "Code/14_char_frequency.py"
)

frequency_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frequency_module)

character_frequency = frequency_module.character_frequency

assert character_frequency("hello") == {
    "h": 1, "e": 1, "l": 2, "o": 1
}
assert character_frequency("banana") == {
    "b": 1, "a": 3, "n": 2
}
assert character_frequency("aaa") == {"a": 3}
assert character_frequency("") == {}
assert character_frequency("123") == {
    "1": 1, "2": 1, "3": 1
}

print("All test cases passed.")
