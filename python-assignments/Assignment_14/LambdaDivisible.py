
CheckDivisibility = lambda x : (x % 5 == 0)

def main():
    x = int(input("enter number : "))
    ret = False

    ret = CheckDivisibility(x)
    if ret == True:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

if __name__ == "__main__":
    main()
    