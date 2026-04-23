
def Reverse(No):
    n = str(No)
    reversed_n = n[::-1]
    return reversed_n



def main():
    No = 123
    result = Reverse(No)
    print(result)


if __name__ == "__main__":
    main()