
def SumofDigits(No):
     sum = 0
     while No > 0:
        digit = No % 10
        sum = sum + digit
        No = No // 10
     return sum

def main():
    No = 123
    result = SumofDigits(No)
    print(result)

if __name__ == "__main__":
    main()