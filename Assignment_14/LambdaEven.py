
CheckEven = lambda x : (x % 2 == 0)

def main():
    x = int(input("enter number : "))
    ret = False

    ret = CheckEven(x)
    if ret == True:
        print("Even")
    else:
        print("Not Even")

if __name__ == "__main__":
    main()
