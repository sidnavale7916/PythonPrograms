
def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


if __name__ == "__main__":
    print(count_vowels_consonants("Hello World"))
    print(count_vowels_consonants("Python"))