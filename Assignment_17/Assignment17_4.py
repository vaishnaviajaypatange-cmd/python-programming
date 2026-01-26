
def AddFactor(No):
    add = 0
    for i in range(1, No):
        if No % i == 0:
            add = add + i
    return add



def main():
    No = int(input("enter no : "))
    result = AddFactor(No)
    print(result)



if __name__ == "__main__":
    main()