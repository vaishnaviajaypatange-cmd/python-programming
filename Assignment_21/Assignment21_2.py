import threading

def Maximum(data):
    max_no = data[0]
    for i in data:
        if i > max_no:
            max_no = i
    print("Maximum element:", max_no)


def Minimum(data):
    min_no = data[0]
    for i in data:
        if i < min_no:
            min_no = i
    print("Minimum element:", min_no)


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    t1 = threading.Thread(target=Maximum, args=(data,))
    t2 = threading.Thread(target=Minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
