def AddDigits(value):
    total = 0
    for digit in value:
        total = total + int(digit)
    return total


def main():
    number = input("Enter number: ")
    result = AddDigits(number)
    print("Addition of digits : ", result)


if __name__ == "__main__":
    main()
