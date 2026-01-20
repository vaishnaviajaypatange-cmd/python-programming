def SumNatural(No):
    sum = 0
    for i in range(1,No+1):
        sum =  sum + i
    return sum


def main():
    No = 5
    result = SumNatural(No)
    print(result)




if __name__ == "__main__":
    main()