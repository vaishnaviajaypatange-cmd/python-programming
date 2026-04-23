from functools import reduce


def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        data.append(int(input("Enter element: ")))

    result = reduce(lambda a, b: a + b, data)
    print("Addition of all elements is:", result)


if __name__ == "__main__":
    main()
