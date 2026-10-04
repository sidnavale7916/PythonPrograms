
def character_frequency(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


if __name__ == "__main__":
    print(character_frequency("hello"))
    print(character_frequency("banana"))