
CheckOdd = lambda x : (x % 2 != 0)

def main():
    x = int(input("enter number : "))
    ret = False

    ret = CheckOdd(x)
    if ret == True:
        print("Odd")
    else:
        print("Not Odd")

if __name__ == "__main__":
    main()
    