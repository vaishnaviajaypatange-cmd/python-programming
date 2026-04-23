
MinNo = lambda x,y : (x < y)

def main():
     x = int(input("enter first number : "))
     y = int(input("enter second number : "))
     Ret = False

     Ret = MinNo(x,y)
     if Ret == True:
        print("Minimum number : ",x)
     else:
        print("Minimum number : ",y)

if __name__ == "__main__":
    main()