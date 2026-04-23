import threading

def EvenList(data):
    total = 0
    print("Even elements:")
    for i in data:
        if i % 2 == 0:
            print(i)
            total += i
    print("Sum of even elements:", total)


def OddList(data):
    total = 0
    print("Odd elements:")
    for i in data:
        if i % 2 != 0:
            print(i)
            total += i
    print("Sum of odd elements:", total)


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    t1 = threading.Thread(target=EvenList, args=(data,))
    t2 = threading.Thread(target=OddList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
