def pattern(No):
    for i in range(1, No + 1):          
        for j in range(1, i + 1):       
            print(j, end=" ")
        print()


def main():
    No = int(input("Enter number: "))
    pattern(No)


if __name__ == "__main__":
    main()
