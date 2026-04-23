
def Add(No1,No2):
    return No1 + No2
    


def main():
    Value1 = int(input("Enter first Number : "))
    Value2 = int(input("Enter second Number : "))
    result = Add(Value1,Value2)
    print("Addition : ",result)


if __name__ == "__main__":
    main()
