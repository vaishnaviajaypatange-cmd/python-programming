import threading

def Even():
    for i in range(1, 21):
        if i % 2 == 0:
            print("Even:", i)

def Odd():
    for i in range(1, 21):
        if i % 2 != 0:
            print("Odd :", i)


def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
