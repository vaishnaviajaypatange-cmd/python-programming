def MinList(data):
    min_no = data[0]
    for i in data:
        if i < min_no:
            min_no = i
    return min_no


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    result = MinList(data)
    print(result)


if __name__ == "__main__":
    main()
