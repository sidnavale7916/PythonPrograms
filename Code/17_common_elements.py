
def common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)

    return result


if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(common_elements([10, 20, 30], [20, 30, 40]))