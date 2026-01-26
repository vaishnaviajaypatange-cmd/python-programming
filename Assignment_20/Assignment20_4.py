import threading

def Small(string):
    count = 0
    for ch in string:
        if ch.islower():
            count += 1
    print("Small Thread")
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase count:", count)
    print()


def Capital(string):
    count = 0
    for ch in string:
        if ch.isupper():
            count += 1
    print("Capital Thread")
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase count:", count)
    print()


def Digits(string):
    count = 0
    for ch in string:
        if ch.isdigit():
            count += 1
    print("Digits Thread")
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digit count:", count)
    print()


def main():
    string = input("Enter string: ")

    t1 = threading.Thread(target=Small, args=(string,), name="Small")
    t2 = threading.Thread(target=Capital, args=(string,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(string,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
