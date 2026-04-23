
def Even(No):
    for i in range(1,No):
        if i % 2 == 0:
            print(i)
    

def main():
    Value = 21
    Even(Value)

if __name__ == "__main__":
    main()