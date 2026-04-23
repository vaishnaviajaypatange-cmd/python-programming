
def CheckPrime(No):
    if (No < 2):
         return "not prime"
    for i in range(2,No):
        if (No % i == 0):
                return "Not Prime"
    else:
        return "Prime"



def main():
    No = 11

    result = CheckPrime(No)
    print(result)
    
    
        

if __name__ == "__main__":
    main()