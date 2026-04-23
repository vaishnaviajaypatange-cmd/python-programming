
def Factor(Value,i):
    if Value % i == 0:
        return True
    else:
        return False
    
    
def main():
    No = 12

    for i in range(1,No+1):
        if Factor(No,i):
            print(i)
  



if __name__ == "__main__":
    main()