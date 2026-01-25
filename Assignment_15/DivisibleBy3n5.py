def main():
    size = int(input("Enter number of elements: "))
    data = []

    for i in range(size):
        data.append(int(input("Enter element: ")))  

    result = list(filter(lambda s: s % 3 == 0 and s % 5 == 0, data))
    print("Elements divisible by 3 and 5:", result)


if __name__ == "__main__":
    main()
