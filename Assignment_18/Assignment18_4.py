def Frequency(data, search):
    count = 0
    for i in data:
        if i == search:
            count = count + 1
    return count


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    search = int(input("Enter element to search: "))
    result = Frequency(data, search)
    print("Frequency:", result)


if __name__ == "__main__":
    main()
