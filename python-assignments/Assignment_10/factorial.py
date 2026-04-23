def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact*i
    return fact


def main():
    No = 5
    result = Factorial(No)
    print(result)


if __name__ == "__main__":
    main()