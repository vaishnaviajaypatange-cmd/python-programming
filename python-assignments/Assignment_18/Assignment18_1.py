def AddList(data):
    total = 0
    for i in data:
        total = total + i
    return total


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    result = AddList(data)
    print("Addition:", result)


if __name__ == "__main__":
    main()
