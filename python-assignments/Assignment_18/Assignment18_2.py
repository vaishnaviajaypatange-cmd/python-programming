def MaxList(data):
    max_no = data[0]
    for i in data:
        if i > max_no:
            max_no = i
    return max_no


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    result = MaxList(data)
    print(result)


if __name__ == "__main__":
    main()
