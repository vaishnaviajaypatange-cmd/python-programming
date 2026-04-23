
Even = lambda data : (data % 2 == 0)

def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        data.append(int(input("Enter element: ")))

    Fdata = list(filter(Even, data))
    print("Even Numbers : ",Fdata)


if __name__ == "__main__":
    main()