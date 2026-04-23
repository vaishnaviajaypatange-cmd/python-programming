from functools import reduce

Max_element = lambda numbers: reduce(lambda a, b: a if a > b else b, numbers)


def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        value = int(input("Enter element : "))
        data.append(value)

    result = Max_element(data)
    print("maximum elements is:", result)


if __name__ == "__main__":
    main()
