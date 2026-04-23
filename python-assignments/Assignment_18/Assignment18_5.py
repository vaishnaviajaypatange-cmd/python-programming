def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False
    return True


def ListPrime(data):
    total = 0
    for i in data:
        if ChkPrime(i):
            total = total + i
    return total


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    result = ListPrime(data)
    print("Addition of prime numbers:", result)


if __name__ == "__main__":
    main()
