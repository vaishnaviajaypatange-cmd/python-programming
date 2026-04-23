
MAxNo = lambda x,y : (x > y)

def main():
     x = int(input("enter first number : "))
     y = int(input("enter second number : "))
     Ret = False

     Ret = MAxNo(x,y)
     if Ret == True:
        print("Maximum number : ",x)
     else:
        print("Maximum number : ",y)

if __name__ == "__main__":
    main()