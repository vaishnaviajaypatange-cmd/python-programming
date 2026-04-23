from functools import reduce

Product = lambda numbers: reduce(lambda a, b: a * b, numbers)


def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        value = int(input("Enter element : "))
        data.append(value)

    result = Product(data)
    print("Product of all elements is:", result)


if __name__ == "__main__":
    main()
