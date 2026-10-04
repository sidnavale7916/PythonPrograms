
def word_frequency(sentence):
    frequency = {}

    words = sentence.lower().split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    print(word_frequency("hello world hello"))
    print(word_frequency("python is easy python is powerful"))