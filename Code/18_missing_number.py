
def find_missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5], 5))
    print(find_missing_number([1, 3, 4, 5], 5))