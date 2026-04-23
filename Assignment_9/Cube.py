def Cube(No):
    return No ** 3
def main():
    print("Enter the number : ")
    No = int(input())
    result = Cube(No)
    print("Cube : ",result)



if __name__ == "__main__":
    main()