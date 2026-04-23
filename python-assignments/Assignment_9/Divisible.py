def Divisible(No):
    if (No % 3 == 0) and (No % 5 == 0):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")


def main():
    No = 15
    Divisible(No)


if __name__ == "__main__":
    main()