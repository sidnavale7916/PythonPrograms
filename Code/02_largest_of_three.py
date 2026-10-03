def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


if __name__ == "__main__":
    print(largest_of_three(10, 25, 15))
    print(largest_of_three(50, 20, 30))