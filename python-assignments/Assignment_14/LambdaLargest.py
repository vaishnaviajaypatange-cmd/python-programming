
largest_no = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)


def main():
     a = int(input("enter first number : "))
     b = int(input("enter second number : "))
     c = int(input("enter third number : "))
     
     Ret = largest_no(a, b, c)
     print("Largest number is:", Ret)


if __name__ == "__main__":
    main()