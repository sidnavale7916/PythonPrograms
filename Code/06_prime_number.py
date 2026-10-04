
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime(7))
    print(is_prime(10))