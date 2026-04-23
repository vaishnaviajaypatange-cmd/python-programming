import threading

sum_result = 0
product_result = 1

def SumList(data):
    global sum_result
    for i in data:
        sum_result += i


def ProductList(data):
    global product_result
    for i in data:
        product_result *= i


def main():
    n = int(input("Enter number of elements: "))
    data = []

    for i in range(n):
        data.append(int(input("Enter element: ")))

    t1 = threading.Thread(target=SumList, args=(data,))
    t2 = threading.Thread(target=ProductList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)


if __name__ == "__main__":
    main()
