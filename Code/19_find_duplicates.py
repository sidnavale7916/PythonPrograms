
def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
    print(find_duplicates([10, 10, 20, 30, 20]))