
import importlib.util

spec = importlib.util.spec_from_file_location(
    "word_frequency",
    "Code/20_word_frequency.py"
)

word_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(word_module)

word_frequency = word_module.word_frequency

assert word_frequency("hello world hello") == {
    "hello": 2, "world": 1
}
assert word_frequency("python is easy python is powerful") == {
    "python": 2, "is": 2, "easy": 1, "powerful": 1
}
assert word_frequency("apple apple apple") == {
    "apple": 3
}
assert word_frequency("") == {}
assert word_frequency("Hello hello HELLO") == {
    "hello": 3
}
assert word_frequency("one two three") == {
    "one": 1, "two": 1, "three": 1
}

print("All test cases passed.")