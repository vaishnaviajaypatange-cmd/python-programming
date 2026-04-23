
def ChkNum(No):
    if (No % 2 == 0):
        return "Even number"
    else:
        return "Odd number"


def main():
    Value = int(input("Enter the Number : "))
    result = ChkNum(Value)
    print(result)


if __name__ == "__main__":
    main()
