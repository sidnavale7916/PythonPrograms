
def fibonacci_series(n):
    if n <= 0:
        return []

    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    print(fibonacci_series(7))
    print(fibonacci_series(5))