def DecimaltoBinary(no):
    binary = ""
    while no > 0:
        binary = str(no % 2) + binary
        no = no // 2
    return binary



def main():
    No = int(input("Enter Number : "))
    
    result = DecimaltoBinary(No)
    print(result)



if __name__ == "__main__":
    main()
