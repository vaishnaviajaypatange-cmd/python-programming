
def PerfectNumber(No):
    sum = 0
    for i in range(1,No):
        if (No % i == 0):
            sum = sum + i
    return sum
    
    
    
def main():
    No = 6
    result = PerfectNumber(No)

    if result == No:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


 
if __name__ == "__main__":
    main()