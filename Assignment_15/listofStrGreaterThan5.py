def main():
    size = int(input("Enter number of strings: "))
    data = []

    for i in range(size):
        data.append(input("Enter string: "))

    result = list(filter(lambda s: len(s) > 5, data))
    print("Strings with length greater than 5:", result)


if __name__ == "__main__":
    main()
