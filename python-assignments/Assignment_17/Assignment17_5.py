def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False
    return True


def main():
    No = int(input("Enter number: "))

    if CheckPrime(No):
        print("It is Prime Number")
    else:
        print("Not Prime Number")


if __name__ == "__main__":
    main()
