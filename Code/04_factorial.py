
def factorial(num):
    if num < 0:
        return "Invalid input"

    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(0))
    print(factorial(3))