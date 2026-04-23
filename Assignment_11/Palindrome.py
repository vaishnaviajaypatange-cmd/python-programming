
def Palindrome(No):
    n = str(No)
    reversed_n = n[::-1]
    if n == reversed_n:
        return "Palindrome"
    else:
        return "Not a Palindrome"



def main():
    No = 121
    result = Palindrome(No)
    print(result)


if __name__ == "__main__":
    main()