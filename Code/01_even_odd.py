def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    print(even_odd(20))
    print(even_odd(11))