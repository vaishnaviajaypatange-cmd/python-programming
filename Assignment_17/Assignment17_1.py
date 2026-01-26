import Arithmetic

def main():
    Value1 = int(input("Enter first Number : "))
    Value2 = int(input("Enter second Number : "))

    print("Addition : ",Arithmetic.Add(Value1,Value2))
    print("Subtraction : ",Arithmetic.Sub(Value1,Value2))
    print("Multiplication : ",Arithmetic.Mult(Value1,Value2))
    print("Division : ",Arithmetic.Div(Value1,Value2))

if __name__ =="__main__":
    main()