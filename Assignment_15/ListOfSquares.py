
square = lambda data : data**2

def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        data.append(int(input("Enter element: ")))

    
    Mdata = list(map(square,data))
    print("Square : ",Mdata)


if __name__ == "__main__":
    main()