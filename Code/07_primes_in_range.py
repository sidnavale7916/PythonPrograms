
def primes_in_range(start, end):
    primes = []

    for num in range(start, end + 1):
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


if __name__ == "__main__":
    print(primes_in_range(1, 10))
    print(primes_in_range(10, 20))