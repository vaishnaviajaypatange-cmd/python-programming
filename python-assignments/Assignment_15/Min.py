from functools import reduce

min_element = lambda numbers: reduce(lambda a, b: a if a < b else b, numbers)


def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        value = int(input("Enter element : "))
        data.append(value)

    result = min_element(data)
    print("Minimum element is:", result)


if __name__ == "__main__":
    main()
