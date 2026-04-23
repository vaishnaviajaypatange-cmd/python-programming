from functools import reduce

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def ProcessList(data):
    fdata = list(filter(is_prime, data))
    mdata = list(map(lambda x: x * 2, fdata))
    rdata = reduce(lambda a, b: a if a > b else b, mdata)
    return fdata,mdata,rdata


def main():
    data = [2, 70, 11, 10, 17, 23, 31, 77]
    f, m, r = ProcessList(data)

    print("Input List =", data)
    print("List after filter =", f)
    print("List after map =", m)
    print("Output of reduce =", r)


if __name__ == "__main__":
    main()
