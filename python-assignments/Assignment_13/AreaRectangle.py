def Area(length,width):
    return length * width


def main():
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))

    result = Area(length,width)
    print("Area of the Rectangle :",result)


if __name__ == "__main__":
    main()