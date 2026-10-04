
def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]


if __name__ == "__main__":
    print(second_largest([10, 20, 4, 45, 99]))
    print(second_largest([5, 5, 3, 2]))