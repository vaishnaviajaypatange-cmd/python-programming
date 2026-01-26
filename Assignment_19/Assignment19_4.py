from functools import reduce

def ProcessList(data):
    fdata = list(filter(lambda x: x % 2 == 0, data))
    mdata = list(map(lambda x: x * x, fdata))
    rdata = reduce(lambda a, b: a + b, mdata)
    return fdata,mdata,rdata


def main():
    data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    f, m, r = ProcessList(data)

    print("Input List =", data)
    print("List after filter =", f)
    print("List after map =", m)
    print("Output of reduce =", r)


if __name__ == "__main__":
    main()
