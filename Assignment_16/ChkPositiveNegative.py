
def check(No):
    if No == 0:
        return "Zero"
    elif No > 0 :
        return "Positive Number"
    else :
        return "Negative Number"


def main():
    Value = int(input("Enter Number : "))
    Result = check(Value)
    print(Result)

if __name__ == "__main__":
    main()