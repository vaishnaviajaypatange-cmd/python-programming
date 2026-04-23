def Operation(a,b):
    Add = a + b
    sub = a - b
    Multiply = a * b
    divide = a / b
    return Add,sub,Multiply,divide

def main():
    No1 = int(input("enter first number : "))
    No2 = int(input("enter second number : "))

    sum,sub,multiply,diff = Operation(No1,No2)
    print("Addition : ",sum)
    print("Subtraction :",sub)
    print("Multiplication :",multiply)
    print("Division :",diff)
   

if __name__ == "__main__":
    main()