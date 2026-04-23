import threading

def isPrime(No):
    if No < 2:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True


def Prime(data):
    print("Prime numbers:")
    for i in data:
        if isPrime(i):
            print(i)


def NonPrime(data):
    print("Non-prime numbers:")
    for i in data:
        if not isPrime(i):
            print(i)


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
