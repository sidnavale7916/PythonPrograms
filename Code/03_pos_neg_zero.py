
def pos_neg_zero(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


if __name__ == "__main__":
    print(pos_neg_zero(10))
    print(pos_neg_zero(-5))
    print(pos_neg_zero(0))