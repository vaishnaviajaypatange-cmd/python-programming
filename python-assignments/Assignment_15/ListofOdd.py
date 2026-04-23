
odd = lambda data : data % 2 != 0

def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        data.append(int(input("Enter element: ")))

    fdata = list(filter(odd,data))
    print("odd numbers : ",fdata)


if __name__ == "__main__":
    main()