import threading

def EvenFactor(No):
    total = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print("Even Factor:", i)
            total += i
    print("Sum of even factors:", total)


def OddFactor(No):
    total = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print("Odd Factor:", i)
            total += i
    print("Sum of odd factors:", total)


def main():
    No = int(input("Enter number: "))

    t1 = threading.Thread(target=EvenFactor, args=(No,))
    t2 = threading.Thread(target=OddFactor, args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
